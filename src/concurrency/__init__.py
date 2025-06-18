"""Concurrency sub-package for Python threading and asyncio demonstrations.

This package demonstrates comprehensive concurrency features available in Python,
including traditional threading, multiprocessing, asyncio, and concurrent.futures.
"""

from .asyncio_demo import demo_asyncio
from .concurrent_futures_demo import demo_concurrent_futures
from .multiprocessing_demo import demo_multiprocessing
from .threading_demo import demo_threading

__version__ = "0.1.0"

__all__ = [
    "demo_threading",
    "demo_asyncio",
    "demo_multiprocessing",
    "demo_concurrent_futures",
    "demo_concurrency",
]


def demo_concurrency() -> None:
    """Demonstrate all Python concurrency features."""
    print("=" * 60)
    print("PYTHON CONCURRENCY DEMONSTRATIONS")
    print("=" * 60)

    demo_threading()
    demo_asyncio()
    demo_multiprocessing()
    demo_concurrent_futures()

    print("=" * 60)
    print("CONCURRENCY DEMONSTRATIONS COMPLETED")
    print("=" * 60)
