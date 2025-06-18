"""
Multiprocessing demonstrations for Python.

This module demonstrates multiprocessing concepts including:
- Process creation and management
- Inter-process communication (queues, pipes)
- Process pools
- Shared memory and locks
- CPU-bound task parallelization
- Process synchronization
"""

import multiprocessing as mp
import os
import random
import time
from typing import List, Tuple


def worker_process(name: str, work_time: float, result_queue: mp.Queue) -> None:
    """Worker process function."""
    print(f"Process {name} (PID: {os.getpid()}) starting work...")
    time.sleep(work_time)
    result = f"Process {name} completed work in {work_time:.2f}s"
    result_queue.put(result)
    print(f"Process {name} finished")


def cpu_intensive_task(n: int) -> Tuple[int, int]:
    """CPU-intensive task for multiprocessing demonstration."""
    process_id = os.getpid()
    result = 0
    for i in range(n):
        result += i * i
    return result, process_id


def square_number(x: int) -> int:
    """Simple function to square a number."""
    time.sleep(0.1)  # Simulate some work
    return x * x


def fibonacci(n: int) -> int:
    """Calculate fibonacci number (CPU-intensive)."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def increment_shared_counter(shared_value, lock, times: int, process_name: str) -> None:
    """Increment shared counter multiple times."""
    for _ in range(times):
        with lock:
            current = shared_value.value
            time.sleep(0.001)  # Simulate work
            shared_value.value = current + 1
    print(f"Process {process_name} finished incrementing")


def producer_process(queue: mp.Queue, name: str, items: int) -> None:
    """Producer process for queue demonstration."""
    for i in range(items):
        item = f"{name}-item-{i}"
        queue.put(item)
        print(f"Producer {name} produced: {item}")
        time.sleep(random.uniform(0.1, 0.3))
    print(f"Producer {name} finished")


def consumer_process(queue: mp.Queue, name: str) -> None:
    """Consumer process for queue demonstration."""
    while True:
        try:
            item = queue.get(timeout=2.0)
            if item is None:  # Poison pill
                break
            print(f"Consumer {name} consumed: {item}")
            time.sleep(random.uniform(0.2, 0.4))
        except Exception:
            break
    print(f"Consumer {name} finished")


def pipe_sender(conn, data: List[str]) -> None:
    """Send data through pipe."""
    for item in data:
        conn.send(item)
        print(f"Sent: {item}")
        time.sleep(0.2)
    conn.close()


def pipe_receiver(conn) -> None:
    """Receive data through pipe."""
    while True:
        try:
            item = conn.recv()
            print(f"Received: {item}")
        except EOFError:
            break
    conn.close()


def demo_multiprocessing() -> None:
    """Demonstrate multiprocessing concepts."""
    print("\n" + "=" * 50)
    print("MULTIPROCESSING DEMONSTRATION")
    print("=" * 50)

    try:
        demo_basic_processes()
        demo_process_communication()
        demo_process_pools()
        demo_shared_memory()
        demo_cpu_bound_comparison()
        demo_pipe_communication()
    except Exception as e:
        print(f"Multiprocessing demonstration encountered an error: {e}")
        print(
            "This is often due to pickling issues when running from imported modules."
        )
        print("For full multiprocessing functionality, run the module directly.")


def demo_basic_processes() -> None:
    """Demonstrate basic process creation and management."""
    print("\n1. Basic Process Creation:")
    print("-" * 25)

    # Create result queue for communication
    result_queue = mp.Queue()
    processes = []

    # Create and start processes
    for i in range(3):
        process = mp.Process(
            target=worker_process,
            args=(f"P{i}", random.uniform(0.5, 1.5), result_queue),
        )
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    # Collect results
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    print("Results from processes:")
    for result in results:
        print(f"  {result}")


def demo_process_communication() -> None:
    """Demonstrate inter-process communication with queues."""
    print("\n2. Process Communication (Queues):")
    print("-" * 33)

    # Create queue for communication
    comm_queue = mp.Queue(maxsize=5)
    processes = []

    # Start producer processes
    for i in range(2):
        producer = mp.Process(target=producer_process, args=(comm_queue, f"P{i}", 5))
        processes.append(producer)
        producer.start()

    # Start consumer processes
    for i in range(2):
        consumer = mp.Process(target=consumer_process, args=(comm_queue, f"C{i}"))
        processes.append(consumer)
        consumer.start()

    # Wait for producers to finish
    for process in processes[:2]:
        process.join()

    # Send poison pills to stop consumers
    for _ in range(2):
        comm_queue.put(None)

    # Wait for consumers to finish
    for process in processes[2:]:
        process.join()


def demo_process_pools() -> None:
    """Demonstrate process pools for parallel execution."""
    print("\n3. Process Pools:")
    print("-" * 15)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Sequential execution
    start_time = time.time()
    sequential_results = [square_number(x) for x in numbers]
    sequential_time = time.time() - start_time

    print(f"Sequential results: {sequential_results}")
    print(f"Sequential time: {sequential_time:.2f}s")

    # Parallel execution with process pool
    start_time = time.time()
    with mp.Pool(processes=4) as pool:
        parallel_results = pool.map(square_number, numbers)
    parallel_time = time.time() - start_time

    print(f"Parallel results: {parallel_results}")
    print(f"Parallel time: {parallel_time:.2f}s")
    print(f"Speedup: {sequential_time / parallel_time:.2f}x")


def demo_shared_memory() -> None:
    """Demonstrate shared memory and synchronization."""
    print("\n4. Shared Memory and Synchronization:")
    print("-" * 37)

    # Create shared memory objects
    manager = mp.Manager()
    shared_value = manager.Value("i", 0)
    lock = manager.Lock()
    processes = []

    # Create processes that increment the shared counter
    for i in range(4):
        process = mp.Process(
            target=increment_shared_counter, args=(shared_value, lock, 25, f"P{i}")
        )
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    final_value = shared_value.value
    print(f"Final counter value: {final_value}")
    print("Expected: 100")


def demo_cpu_bound_comparison() -> None:
    """Compare CPU-bound task performance."""
    print("\n5. CPU-Bound Task Comparison:")
    print("-" * 30)

    # Test data
    numbers = [500000, 600000, 700000, 800000]

    # Sequential execution
    print("Sequential execution:")
    start_time = time.time()
    sequential_results = [cpu_intensive_task(n) for n in numbers]
    sequential_time = time.time() - start_time

    print(f"  Time: {sequential_time:.2f}s")
    for result, pid in sequential_results:
        print(f"  Result: {result}, PID: {pid}")

    # Parallel execution
    print("\nParallel execution:")
    start_time = time.time()
    with mp.Pool(processes=mp.cpu_count()) as pool:
        parallel_results = pool.map(cpu_intensive_task, numbers)
    parallel_time = time.time() - start_time

    print(f"  Time: {parallel_time:.2f}s")
    for result, pid in parallel_results:
        print(f"  Result: {result}, PID: {pid}")

    print(f"Speedup: {sequential_time / parallel_time:.2f}x")
    print(f"CPU cores used: {len(set(pid for _, pid in parallel_results))}")


def demo_pipe_communication() -> None:
    """Demonstrate pipe communication between processes."""
    print("\n6. Pipe Communication:")
    print("-" * 20)

    # Create pipe
    parent_conn, child_conn = mp.Pipe()

    # Data to send
    data = ["message1", "message2", "message3", "message4"]

    # Start sender process
    sender = mp.Process(target=pipe_sender, args=(child_conn, data))
    sender.start()

    # Start receiver process
    receiver = mp.Process(target=pipe_receiver, args=(parent_conn,))
    receiver.start()

    # Wait for processes to complete
    sender.join()
    receiver.join()

    print("Pipe communication completed")
