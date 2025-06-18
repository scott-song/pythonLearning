"""
Asyncio demonstrations for Python.

This module demonstrates asyncio concepts including:
- Basic async/await syntax
- Coroutines and tasks
- Async context managers
- Async generators and iterators
- Concurrent execution with asyncio.gather
- Event loops and scheduling
- Async I/O operations
"""

import asyncio
import random
import time
from typing import Any, AsyncGenerator, Dict


async def simple_coroutine(name: str, delay: float) -> str:
    """Simple coroutine that simulates async work."""
    print(f"Coroutine {name} starting...")
    await asyncio.sleep(delay)
    result = f"Coroutine {name} completed after {delay:.2f}s"
    print(result)
    return result


async def fetch_data(url: str, delay: float) -> Dict[str, Any]:
    """Simulate fetching data from a URL."""
    print(f"Fetching data from {url}...")
    await asyncio.sleep(delay)  # Simulate network delay

    # Simulate response data
    data = {
        "url": url,
        "status": 200,
        "data": f"Response from {url}",
        "timestamp": time.time(),
        "delay": delay,
    }
    print(f"Completed fetching from {url}")
    return data


async def process_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Process fetched data asynchronously."""
    print(f"Processing data from {data['url']}...")
    await asyncio.sleep(0.1)  # Simulate processing time

    processed = {
        **data,
        "processed": True,
        "processed_at": time.time(),
        "word_count": len(data["data"].split()),
    }
    print(f"Processed data from {data['url']}")
    return processed


class AsyncCounter:
    """Async counter with locks."""

    def __init__(self) -> None:
        """Initialize counter with async lock."""
        self._value = 0
        self._lock = asyncio.Lock()

    async def increment(self) -> None:
        """Async increment with lock."""
        async with self._lock:
            current = self._value
            await asyncio.sleep(0.001)  # Simulate async work
            self._value = current + 1

    async def get_value(self) -> int:
        """Get current value."""
        async with self._lock:
            return self._value


class AsyncQueue:
    """Async producer-consumer queue."""

    def __init__(self, maxsize: int = 0) -> None:
        """Initialize async queue."""
        self._queue: asyncio.Queue = asyncio.Queue(maxsize=maxsize)
        self._stop_event = asyncio.Event()

    async def producer(self, name: str, items: int) -> None:
        """Async producer."""
        for i in range(items):
            if self._stop_event.is_set():
                break

            item = f"{name}-item-{i}"
            await self._queue.put(item)
            print(f"Producer {name} produced: {item}")
            await asyncio.sleep(random.uniform(0.1, 0.3))

        print(f"Producer {name} finished")

    async def consumer(self, name: str) -> None:
        """Async consumer."""
        while not self._stop_event.is_set():
            try:
                item = await asyncio.wait_for(self._queue.get(), timeout=1.0)
                print(f"Consumer {name} consumed: {item}")
                await asyncio.sleep(random.uniform(0.2, 0.4))
                self._queue.task_done()
            except asyncio.TimeoutError:
                continue

        print(f"Consumer {name} finished")

    async def stop(self) -> None:
        """Stop producers and consumers."""
        self._stop_event.set()


async def async_generator_example() -> AsyncGenerator[int, None]:
    """Async generator that yields numbers."""
    for i in range(5):
        print(f"Generating {i}")
        await asyncio.sleep(0.2)
        yield i


class AsyncContextManager:
    """Async context manager example."""

    def __init__(self, name: str) -> None:
        """Initialize context manager."""
        self.name = name

    async def __aenter__(self) -> "AsyncContextManager":
        """Async enter."""
        print(f"Entering async context: {self.name}")
        await asyncio.sleep(0.1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async exit."""
        print(f"Exiting async context: {self.name}")
        await asyncio.sleep(0.1)

    async def do_work(self) -> str:
        """Do some async work."""
        await asyncio.sleep(0.2)
        return f"Work completed in {self.name}"


async def cpu_bound_async(n: int) -> int:
    """CPU-bound task with async yields."""
    result = 0
    for i in range(n):
        result += i * i
        if i % 10000 == 0:
            await asyncio.sleep(0)  # Yield control
    return result


def demo_asyncio() -> None:
    """Demonstrate asyncio concepts."""
    print("\n" + "=" * 50)
    print("ASYNCIO DEMONSTRATION")
    print("=" * 50)

    # Run async demos
    asyncio.run(demo_basic_async())
    asyncio.run(demo_concurrent_execution())
    asyncio.run(demo_async_context_manager())
    asyncio.run(demo_async_generator())
    asyncio.run(demo_async_queue_pattern())
    asyncio.run(demo_async_synchronization())
    asyncio.run(demo_error_handling())


async def demo_basic_async() -> None:
    """Demonstrate basic async/await usage."""
    print("\n1. Basic Async/Await:")
    print("-" * 21)

    # Sequential execution
    start_time = time.time()
    result1 = await simple_coroutine("A", 0.5)
    result2 = await simple_coroutine("B", 0.3)
    result3 = await simple_coroutine("C", 0.4)
    sequential_time = time.time() - start_time

    print(f"Sequential execution took: {sequential_time:.2f}s")

    # Concurrent execution
    start_time = time.time()
    results = await asyncio.gather(
        simple_coroutine("X", 0.5),
        simple_coroutine("Y", 0.3),
        simple_coroutine("Z", 0.4),
    )
    concurrent_time = time.time() - start_time

    print(f"Concurrent execution took: {concurrent_time:.2f}s")
    print(f"Speedup: {sequential_time / concurrent_time:.2f}x")


async def demo_concurrent_execution() -> None:
    """Demonstrate concurrent execution patterns."""
    print("\n2. Concurrent Execution:")
    print("-" * 23)

    urls = [
        ("api1.example.com", 0.5),
        ("api2.example.com", 0.8),
        ("api3.example.com", 0.3),
        ("api4.example.com", 0.6),
    ]

    # Fetch data concurrently
    print("Fetching data concurrently:")
    start_time = time.time()

    fetch_tasks = [fetch_data(url, delay) for url, delay in urls]
    fetched_data = await asyncio.gather(*fetch_tasks)

    # Process data concurrently
    process_tasks = [process_data(data) for data in fetched_data]
    processed_data = await asyncio.gather(*process_tasks)

    total_time = time.time() - start_time

    print(f"Processed {len(processed_data)} items in {total_time:.2f}s")
    for data in processed_data:
        print(f"  {data['url']}: {data['word_count']} words")


async def demo_async_context_manager() -> None:
    """Demonstrate async context managers."""
    print("\n3. Async Context Manager:")
    print("-" * 25)

    async with AsyncContextManager("Database") as db:
        result = await db.do_work()
        print(f"Result: {result}")

    # Multiple context managers
    async with AsyncContextManager("Cache") as cache, AsyncContextManager(
        "Logger"
    ) as logger:
        cache_result = await cache.do_work()
        log_result = await logger.do_work()
        print(f"Cache: {cache_result}")
        print(f"Logger: {log_result}")


async def demo_async_generator() -> None:
    """Demonstrate async generators."""
    print("\n4. Async Generator:")
    print("-" * 18)

    print("Consuming async generator:")
    async for value in async_generator_example():
        print(f"Received: {value}")

    # Async comprehension
    print("\nAsync comprehension:")
    squared = [x**2 async for x in async_generator_example()]
    print(f"Squared values: {squared}")


async def demo_async_queue_pattern() -> None:
    """Demonstrate async producer-consumer pattern."""
    print("\n5. Async Producer-Consumer:")
    print("-" * 27)

    queue_manager = AsyncQueue(maxsize=3)

    # Create tasks
    tasks = []

    # Producers
    tasks.append(asyncio.create_task(queue_manager.producer("P1", 5)))
    tasks.append(asyncio.create_task(queue_manager.producer("P2", 3)))

    # Consumers
    tasks.append(asyncio.create_task(queue_manager.consumer("C1")))
    tasks.append(asyncio.create_task(queue_manager.consumer("C2")))

    # Wait for producers to finish
    await asyncio.gather(*tasks[:2])

    # Give consumers time to finish
    await asyncio.sleep(1)
    await queue_manager.stop()

    # Cancel remaining tasks
    for task in tasks[2:]:
        task.cancel()

    await asyncio.gather(*tasks[2:], return_exceptions=True)


async def demo_async_synchronization() -> None:
    """Demonstrate async synchronization."""
    print("\n6. Async Synchronization:")
    print("-" * 24)

    counter = AsyncCounter()

    async def increment_counter(name: str, times: int) -> None:
        for _ in range(times):
            await counter.increment()
        print(f"{name} finished incrementing")

    # Run multiple coroutines incrementing the counter
    tasks = [increment_counter(f"Task-{i}", 20) for i in range(5)]

    await asyncio.gather(*tasks)

    final_value = await counter.get_value()
    print(f"Final counter value: {final_value}")
    print("Expected: 100")


async def demo_error_handling() -> None:
    """Demonstrate async error handling."""
    print("\n7. Async Error Handling:")
    print("-" * 24)

    async def failing_coroutine(name: str, should_fail: bool) -> str:
        await asyncio.sleep(0.1)
        if should_fail:
            raise ValueError(f"Error in {name}")
        return f"Success in {name}"

    # Handle errors with try/except
    try:
        result = await failing_coroutine("test1", True)
    except ValueError as e:
        print(f"Caught error: {e}")

    # Handle errors in gather with return_exceptions
    results = await asyncio.gather(
        failing_coroutine("task1", False),
        failing_coroutine("task2", True),
        failing_coroutine("task3", False),
        return_exceptions=True,
    )

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i+1} failed: {result}")
        else:
            print(f"Task {i+1} succeeded: {result}")

    # Timeout handling
    try:
        await asyncio.wait_for(simple_coroutine("slow", 2.0), timeout=1.0)
    except asyncio.TimeoutError:
        print("Operation timed out after 1 second")
