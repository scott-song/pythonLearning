#!/usr/bin/env python3
"""
Auto-reload script for the Python Learning Project.

Watches for file changes and automatically runs the application.
"""

import subprocess
import sys
import time

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer


class CodeChangeHandler(FileSystemEventHandler):
    """Handler for file system events."""

    def __init__(self) -> None:
        """Initialize the CodeChangeHandler.

        Sets up initial state for tracking file changes and debouncing.
        """
        self.last_run = 0.0
        self.debounce_seconds = 1  # Prevent multiple rapid runs

    def on_modified(self, event: FileSystemEvent) -> None:
        """Handle file modification event.

        Checks if the event is a file modification and if it's a Python file.
        If it's a Python file, it runs the application.
        """
        if event.is_directory:
            return

        # Only watch Python files
        if not str(event.src_path).endswith(".py"):
            return

        # Debounce rapid changes
        current_time = time.time()
        if current_time - self.last_run < self.debounce_seconds:
            return

        self.last_run = current_time
        self.run_application()

    def run_application(self) -> None:
        """Run the main application."""
        print("\n" + "=" * 50)
        print("🔄 File changed! Running application...")
        print("=" * 50)

        try:
            # Run the main application
            result = subprocess.run(
                [sys.executable, "src/main.py"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode == 0:
                print("✅ Application ran successfully!")
                if result.stdout:
                    print("\n📤 Output:")
                    print(result.stdout)
            else:
                print("❌ Application failed!")
                if result.stderr:
                    print("\n🚨 Error:")
                    print(result.stderr)

        except subprocess.TimeoutExpired:
            print("⏰ Application timed out (30s limit)")
        except Exception as e:
            print(f"💥 Error running application: {e}")


def main() -> None:
    """Start the file watcher.

    Sets up the file watcher and runs the application once at startup.
    """
    # Run the application once at startup
    event_handler = CodeChangeHandler()
    print("🚀 Running application at startup...")
    event_handler.run_application()

    path = "."
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("\n" + "=" * 50)
    print("👀 Watching for file changes...")
    print("=" * 50 + "\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n" + "=" * 50)
        print("👋 Stopping file watcher...")
        print("=" * 50 + "\n")

    observer.join()


if __name__ == "__main__":
    main()
