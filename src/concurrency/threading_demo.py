"""
Threading demonstrations for Python.

This module demonstrates threading concepts including:
- Basic thread creation and management
- Thread synchronization with locks, events, conditions
- Thread-safe data structures
- Producer-consumer patterns
- Thread pools
- Daemon threads
"""

import queue
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from typing import List


class Counter:
    """Thread-safe counter using locks."""

    def __init__(self) -> None:
        """Initialize counter with lock."""
        self._value = 0
        self._lock = threading.Lock()

    def increment(self) -> None:
        """Thread-safe increment."""
        with self._lock:
            current = self._value
            # Simulate some work
            time.sleep(0.001)
            self._value = current + 1

    def get_value(self) -> int:
        """Get current value."""
        with self._lock:
            return self._value


class BankAccount:
    """Thread-safe bank account."""

    def __init__(self, initial_balance: float = 0.0) -> None:
        """Initialize account with balance and lock."""
        self._balance = initial_balance
        self._lock = threading.RLock()  # Reentrant lock
        self._transactions: List[str] = []

    def deposit(self, amount: float) -> None:
        """Thread-safe deposit."""
        with self._lock:
            old_balance = self._balance
            time.sleep(0.001)  # Simulate processing time
            self._balance += amount
            self._transactions.append(f"Deposit: +${amount:.2f}")
            print(f"Deposited ${amount:.2f}, Balance: ${self._balance:.2f}")

    def withdraw(self, amount: float) -> bool:
        """Thread-safe withdrawal."""
        with self._lock:
            if self._balance >= amount:
                old_balance = self._balance
                time.sleep(0.001)  # Simulate processing time
                self._balance -= amount
                self._transactions.append(f"Withdrawal: -${amount:.2f}")
                print(f"Withdrew ${amount:.2f}, Balance: ${self._balance:.2f}")
                return True
            else:
                print(f"Insufficient funds for ${amount:.2f}")
                return False

    def get_balance(self) -> float:
        """Get current balance."""
        with self._lock:
            return self._balance

    def transfer(self, other: "BankAccount", amount: float) -> bool:
        """Transfer money to another account."""
        # Acquire locks in consistent order to prevent deadlock
        first_lock = self._lock if id(self) < id(other) else other._lock
        second_lock = other._lock if id(self) < id(other) else self._lock

        with first_lock:
            with second_lock:
                if self._balance >= amount:
                    self._balance -= amount
                    other._balance += amount
                    self._transactions.append(f"Transfer out: -${amount:.2f}")
                    other._transactions.append(f"Transfer in: +${amount:.2f}")
                    print(f"Transferred ${amount:.2f}")
                    return True
                return False


class ProducerConsumer:
    """Producer-Consumer pattern demonstration."""

    def __init__(self, buffer_size: int = 5) -> None:
        """Initialize with bounded queue."""
        self.buffer = queue.Queue(maxsize=buffer_size)
        self.stop_event = threading.Event()

    def producer(self, name: str, items: int) -> None:
        """Producer function."""
        for i in range(items):
            if self.stop_event.is_set():
                break

            item = f"{name}-item-{i}"
            self.buffer.put(item)
            print(f"Producer {name} produced: {item}")
            time.sleep(random.uniform(0.1, 0.3))

        print(f"Producer {name} finished")

    def consumer(self, name: str) -> None:
        """Consumer function."""
        while not self.stop_event.is_set():
            try:
                item = self.buffer.get(timeout=1.0)
                print(f"Consumer {name} consumed: {item}")
                time.sleep(random.uniform(0.2, 0.4))
                self.buffer.task_done()
            except queue.Empty:
                continue

        print(f"Consumer {name} finished")

    def stop(self) -> None:
        """Stop all producers and consumers."""
        self.stop_event.set()


def worker_function(name: str, work_time: float) -> str:
    """Simple worker function for thread demonstrations."""
    print(f"Worker {name} starting work...")
    time.sleep(work_time)
    result = f"Worker {name} completed work in {work_time:.2f}s"
    print(result)
    return result


def cpu_bound_task(n: int) -> int:
    """CPU-intensive task for thread pool demonstration."""
    result = 0
    for i in range(n):
        result += i * i
    return result


def io_bound_task(url: str, delay: float) -> str:
    """Simulate I/O-bound task."""
    print(f"Fetching {url}...")
    time.sleep(delay)  # Simulate network delay
    return f"Data from {url} (delay: {delay:.2f}s)"


def demo_threading() -> None:
    """Demonstrate threading concepts."""
    print("\n" + "=" * 50)
    print("THREADING DEMONSTRATION")
    print("=" * 50)

    demo_basic_threading()
    demo_thread_synchronization()
    demo_thread_safe_counter()
    demo_bank_account_threading()
    demo_producer_consumer()
    demo_thread_pool()
    demo_daemon_threads()


def demo_basic_threading() -> None:
    """Demonstrate basic thread creation and management."""
    print("\n1. Basic Threading:")
    print("-" * 18)

    # Create and start threads
    threads = []
    for i in range(3):
        thread = threading.Thread(
            target=worker_function, args=(f"T{i}", random.uniform(0.5, 1.5))
        )
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All basic threads completed")


def demo_thread_synchronization() -> None:
    """Demonstrate thread synchronization with Event and Condition."""
    print("\n2. Thread Synchronization:")
    print("-" * 25)

    # Event synchronization
    event = threading.Event()

    def waiter(name: str) -> None:
        print(f"{name} waiting for event...")
        event.wait()
        print(f"{name} received event!")

    def setter() -> None:
        time.sleep(1)
        print("Setting event...")
        event.set()

    # Start waiter threads
    waiters = []
    for i in range(3):
        thread = threading.Thread(target=waiter, args=(f"Waiter-{i}",))
        waiters.append(thread)
        thread.start()

    # Start setter thread
    setter_thread = threading.Thread(target=setter)
    setter_thread.start()

    # Wait for completion
    setter_thread.join()
    for thread in waiters:
        thread.join()


def demo_thread_safe_counter() -> None:
    """Demonstrate thread-safe counter with locks."""
    print("\n3. Thread-Safe Counter:")
    print("-" * 22)

    counter = Counter()
    threads = []

    def increment_counter(name: str, times: int) -> None:
        for _ in range(times):
            counter.increment()
        print(f"{name} finished incrementing")

    # Start multiple threads incrementing the counter
    for i in range(5):
        thread = threading.Thread(target=increment_counter, args=(f"Thread-{i}", 20))
        threads.append(thread)
        thread.start()

    # Wait for all threads
    for thread in threads:
        thread.join()

    print(f"Final counter value: {counter.get_value()}")
    print("Expected: 100")


def demo_bank_account_threading() -> None:
    """Demonstrate thread-safe bank account operations."""
    print("\n4. Thread-Safe Bank Account:")
    print("-" * 28)

    account1 = BankAccount(1000.0)
    account2 = BankAccount(500.0)

    def perform_operations() -> None:
        # Multiple concurrent operations
        operations = [
            lambda: account1.deposit(100.0),
            lambda: account1.withdraw(50.0),
            lambda: account2.deposit(200.0),
            lambda: account1.transfer(account2, 150.0),
            lambda: account2.withdraw(75.0),
        ]

        threads = []
        for op in operations:
            thread = threading.Thread(target=op)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    print(
        f"Initial balances - Account1: ${account1.get_balance():.2f}, Account2: ${account2.get_balance():.2f}"
    )
    perform_operations()
    print(
        f"Final balances - Account1: ${account1.get_balance():.2f}, Account2: ${account2.get_balance():.2f}"
    )


def demo_producer_consumer() -> None:
    """Demonstrate producer-consumer pattern."""
    print("\n5. Producer-Consumer Pattern:")
    print("-" * 29)

    pc = ProducerConsumer(buffer_size=3)
    threads = []

    # Start producers
    for i in range(2):
        producer_thread = threading.Thread(target=pc.producer, args=(f"P{i}", 5))
        threads.append(producer_thread)
        producer_thread.start()

    # Start consumers
    for i in range(2):
        consumer_thread = threading.Thread(target=pc.consumer, args=(f"C{i}",))
        consumer_thread.daemon = True  # Daemon thread
        threads.append(consumer_thread)
        consumer_thread.start()

    # Wait for producers to finish
    for thread in threads[:2]:  # Only producers
        thread.join()

    # Give consumers time to finish processing
    time.sleep(2)
    pc.stop()


def demo_thread_pool() -> None:
    """Demonstrate thread pool with ThreadPoolExecutor."""
    print("\n6. Thread Pool Executor:")
    print("-" * 23)

    # I/O-bound tasks
    urls = [
        ("api.example.com", 0.5),
        ("database.local", 0.8),
        ("cache.server", 0.3),
        ("external.api", 1.0),
    ]

    print("I/O-bound tasks with ThreadPoolExecutor:")
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(io_bound_task, url, delay) for url, delay in urls]

        results = [future.result() for future in futures]
        for result in results:
            print(f"  {result}")

    # CPU-bound tasks (not ideal for threading due to GIL)
    print("\nCPU-bound tasks (limited by GIL):")
    numbers = [100000, 200000, 150000, 300000]

    with ThreadPoolExecutor(max_workers=2) as executor:
        start_time = time.time()
        futures = [executor.submit(cpu_bound_task, n) for n in numbers]

        results = [future.result() for future in futures]
        end_time = time.time()

        print(f"  Results: {results}")
        print(f"  Time taken: {end_time - start_time:.2f}s")


def demo_daemon_threads() -> None:
    """Demonstrate daemon threads."""
    print("\n7. Daemon Threads:")
    print("-" * 16)

    def daemon_worker() -> None:
        # Run for a limited time to demonstrate daemon behavior
        for i in range(5):
            print(f"Daemon thread working... ({i+1}/5)")
            time.sleep(0.5)
        print("Daemon thread finished normally")

    def regular_worker() -> None:
        for i in range(3):
            print(f"Regular thread work {i}")
            time.sleep(0.5)
        print("Regular thread finished")

    # Create daemon thread
    daemon_thread = threading.Thread(target=daemon_worker)
    daemon_thread.daemon = True
    daemon_thread.start()

    # Create regular thread
    regular_thread = threading.Thread(target=regular_worker)
    regular_thread.start()

    # Wait for regular thread
    regular_thread.join()

    print("Main thread ending (daemon thread will stop automatically)")
    time.sleep(0.5)  # Brief pause to show daemon stopping
