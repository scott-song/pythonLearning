"""
Concurrent.futures demonstrations for Python.

This module demonstrates concurrent.futures concepts including:
- ThreadPoolExecutor for I/O-bound tasks
- ProcessPoolExecutor for CPU-bound tasks
- Future objects and result handling
- Exception handling in concurrent execution
- Timeout handling
- Callback functions
"""

import concurrent.futures
import random
import time
from typing import Tuple


def io_bound_task(task_id: int, delay: float) -> Tuple[int, str]:
    """Simulate I/O-bound task (e.g., network request, file I/O)."""
    print(f"I/O Task {task_id} starting (delay: {delay:.2f}s)")
    time.sleep(delay)  # Simulate I/O wait
    result = f"I/O Task {task_id} completed"
    print(result)
    return task_id, result


def cpu_bound_task(n: int) -> Tuple[int, int]:
    """CPU-intensive task for ProcessPoolExecutor."""
    print(f"CPU Task starting with n={n}")
    result = sum(i * i for i in range(n))
    print(f"CPU Task with n={n} completed")
    return n, result


def failing_task(task_id: int, should_fail: bool) -> str:
    """Task that may fail for error handling demonstration."""
    time.sleep(0.2)
    if should_fail:
        raise ValueError(f"Task {task_id} failed intentionally")
    return f"Task {task_id} succeeded"


def download_simulation(url: str, size_mb: int) -> Tuple[str, int, float]:
    """Simulate downloading a file."""
    download_time = size_mb * 0.1 + random.uniform(0.1, 0.3)
    print(f"Downloading {url} ({size_mb}MB)...")
    time.sleep(download_time)
    print(f"Downloaded {url}")
    return url, size_mb, download_time


def process_file(filename: str, processing_time: float) -> str:
    """Simulate file processing."""
    print(f"Processing {filename}...")
    time.sleep(processing_time)
    result = f"Processed {filename} in {processing_time:.2f}s"
    print(result)
    return result


def callback_function(future: concurrent.futures.Future) -> None:
    """Callback function for future completion."""
    try:
        result = future.result()
        print(f"Callback: Task completed with result: {result}")
    except Exception as e:
        print(f"Callback: Task failed with error: {e}")


def demo_concurrent_futures() -> None:
    """Demonstrate concurrent.futures concepts."""
    print("\n" + "=" * 50)
    print("CONCURRENT.FUTURES DEMONSTRATION")
    print("=" * 50)

    demo_thread_pool_executor()
    demo_process_pool_executor()
    demo_future_handling()
    demo_exception_handling()
    demo_timeout_handling()
    demo_callback_functions()
    demo_as_completed()


def demo_thread_pool_executor() -> None:
    """Demonstrate ThreadPoolExecutor for I/O-bound tasks."""
    print("\n1. ThreadPoolExecutor (I/O-bound):")
    print("-" * 32)

    # I/O-bound tasks with different delays
    tasks = [(i, random.uniform(0.5, 1.5)) for i in range(5)]

    # Sequential execution
    start_time = time.time()
    sequential_results = [io_bound_task(task_id, delay) for task_id, delay in tasks]
    sequential_time = time.time() - start_time

    print(f"Sequential execution time: {sequential_time:.2f}s")

    # Concurrent execution with ThreadPoolExecutor
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(io_bound_task, task_id, delay) for task_id, delay in tasks
        ]
        concurrent_results = [future.result() for future in futures]

    concurrent_time = time.time() - start_time

    print(f"Concurrent execution time: {concurrent_time:.2f}s")
    print(f"Speedup: {sequential_time / concurrent_time:.2f}x")


def demo_process_pool_executor() -> None:
    """Demonstrate ProcessPoolExecutor for CPU-bound tasks."""
    print("\n2. ProcessPoolExecutor (CPU-bound):")
    print("-" * 33)

    # CPU-bound tasks
    numbers = [100000, 200000, 150000, 300000]

    # Sequential execution
    start_time = time.time()
    sequential_results = [cpu_bound_task(n) for n in numbers]
    sequential_time = time.time() - start_time

    print(f"Sequential execution time: {sequential_time:.2f}s")
    print("Sequential results:")
    for n, result in sequential_results:
        print(f"  n={n}: result={result}")

    # Parallel execution with ProcessPoolExecutor
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(cpu_bound_task, n) for n in numbers]
        parallel_results = [future.result() for future in futures]

    parallel_time = time.time() - start_time

    print(f"Parallel execution time: {parallel_time:.2f}s")
    print("Parallel results:")
    for n, result in parallel_results:
        print(f"  n={n}: result={result}")

    print(f"Speedup: {sequential_time / parallel_time:.2f}x")


def demo_future_handling() -> None:
    """Demonstrate Future object handling."""
    print("\n3. Future Object Handling:")
    print("-" * 25)

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks and get futures
        futures = []
        for i in range(4):
            future = executor.submit(io_bound_task, i, random.uniform(0.3, 0.8))
            futures.append(future)

        # Check future states
        print("Future states after submission:")
        for i, future in enumerate(futures):
            print(f"  Future {i}: running={future.running()}, done={future.done()}")

        # Wait for completion and get results
        print("\nWaiting for completion...")
        for i, future in enumerate(futures):
            task_id, result = future.result()  # Blocks until completion
            print(f"  Future {i} result: {result}")


def demo_exception_handling() -> None:
    """Demonstrate exception handling in concurrent execution."""
    print("\n4. Exception Handling:")
    print("-" * 20)

    # Mix of successful and failing tasks
    task_configs = [
        (1, False),  # Success
        (2, True),  # Fail
        (3, False),  # Success
        (4, True),  # Fail
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures = [
            executor.submit(failing_task, task_id, should_fail)
            for task_id, should_fail in task_configs
        ]

        for i, future in enumerate(futures):
            try:
                result = future.result()
                print(f"Task {i+1}: {result}")
            except Exception as e:
                print(f"Task {i+1}: Error - {e}")


def demo_timeout_handling() -> None:
    """Demonstrate timeout handling."""
    print("\n5. Timeout Handling:")
    print("-" * 18)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Submit tasks with different durations
        futures = [
            executor.submit(io_bound_task, 1, 0.5),  # Fast task
            executor.submit(io_bound_task, 2, 2.0),  # Slow task
        ]

        for i, future in enumerate(futures):
            try:
                task_id, result = future.result(timeout=1.0)  # 1 second timeout
                print(f"Task {i+1}: {result}")
            except concurrent.futures.TimeoutError:
                print(f"Task {i+1}: Timed out after 1 second")
                future.cancel()  # Try to cancel (may not work if already running)


def demo_callback_functions() -> None:
    """Demonstrate callback functions."""
    print("\n6. Callback Functions:")
    print("-" * 20)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Submit tasks with callbacks
        futures = []
        for i in range(3):
            future = executor.submit(io_bound_task, i, random.uniform(0.3, 0.7))
            future.add_done_callback(callback_function)
            futures.append(future)

        # Wait for all to complete
        concurrent.futures.wait(futures)
        print("All tasks with callbacks completed")


def demo_as_completed() -> None:
    """Demonstrate as_completed for processing results as they finish."""
    print("\n7. Processing Results as Completed:")
    print("-" * 35)

    # Simulate downloading multiple files
    downloads = [
        ("file1.zip", 10),
        ("file2.pdf", 5),
        ("file3.mp4", 25),
        ("file4.txt", 1),
        ("file5.iso", 50),
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit all download tasks
        future_to_url = {
            executor.submit(download_simulation, url, size): url
            for url, size in downloads
        }

        # Process results as they complete
        completed_downloads = 0
        total_size = 0

        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                file_url, size_mb, download_time = future.result()
                completed_downloads += 1
                total_size += size_mb
                print(
                    f"Completed {completed_downloads}/{len(downloads)}: "
                    f"{file_url} ({size_mb}MB in {download_time:.2f}s)"
                )
            except Exception as e:
                print(f"Download {url} failed: {e}")

        print(f"All downloads completed. Total size: {total_size}MB")
