#!/usr/bin/env python3
"""
Auto-reload script for the Python Learning Project.
Watches for file changes and automatically runs the application.
"""

import sys
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class CodeChangeHandler(FileSystemEventHandler):
    """Handler for file system events."""

    def __init__(self):
        self.last_run = 0
        self.debounce_seconds = 1  # Prevent multiple rapid runs

    def on_modified(self, event):
        """Called when a file is modified."""
        if event.is_directory:
            return

        # Only watch Python files
        if not str(event.src_path).endswith('.py'):
            return

        # Debounce rapid changes
        current_time = time.time()
        if current_time - self.last_run < self.debounce_seconds:
            return

        self.last_run = current_time
        self.run_application()

    def run_application(self):
        """Run the main application."""
        print("\n" + "="*50)
        print("🔄 File changed! Running application...")
        print("="*50)

        try:
            # Run the main application
            result = subprocess.run([
                sys.executable, "src/main.py"
            ], capture_output=True, text=True, timeout=30)

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

        print("="*50)
        print("👀 Watching for changes... (Ctrl+C to stop)")


def main():
    """Main function to start the file watcher."""
    print("🚀 Starting Python Learning Project Auto-Reload")
    print("👀 Watching for changes in src/ and tests/ directories...")
    print("Press Ctrl+C to stop\n")

    # Create event handler and observer
    event_handler = CodeChangeHandler()
    observer = Observer()

    # Watch src and tests directories
    observer.schedule(event_handler, "src", recursive=True)
    observer.schedule(event_handler, "tests", recursive=True)

    # Start watching
    observer.start()

    # Run the application once at startup
    event_handler.run_application()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping file watcher...")
        observer.stop()

    observer.join()
    print("👋 Auto-reload stopped!")


if __name__ == "__main__":
    main()
