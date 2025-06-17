"""Utility functions for configuration and logging operations."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


def read_config_file(config_path: str) -> Optional[Dict[str, Any]]:
    """Read configuration from a JSON file.

    Args:
        config_path: Path to the configuration file

    Returns:
        Dictionary containing configuration data, or None if error
    """
    try:
        config_file = Path(config_path)
        if config_file.exists():
            with open(config_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, dict) else None
        else:
            print(f"Configuration file {config_path} not found")
            return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON configuration: {e}")
        return None
    except Exception as e:
        print(f"Error reading configuration file: {e}")
        return None


def write_log_entry(log_path: str, message: str, level: str = "INFO") -> bool:
    """Write a log entry to a file.

    Args:
        log_path: Path to the log file
        message: Log message to write
        level: Log level (INFO, WARNING, ERROR, etc.)

    Returns:
        True if successful, False otherwise
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}\n"

        with open(log_path, "a", encoding="utf-8") as file:
            file.write(log_entry)
        return True
    except Exception as e:
        print(f"Error writing to log file: {e}")
        return False


def create_sample_config(config_path: str) -> bool:
    """Create a sample configuration file.

    Args:
        config_path: Path where to create the configuration file

    Returns:
        True if successful, False otherwise
    """
    sample_config = {
        "app_name": "Python Learning Demo",
        "version": "1.0.0",
        "debug": True,
        "log_level": "INFO",
        "database": {"host": "localhost", "port": 5432, "name": "demo_db"},
        "features": {"auto_save": True, "notifications": False},
    }

    try:
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump(sample_config, file, indent=2)
        return True
    except Exception as e:
        print(f"Error creating sample configuration: {e}")
        return False
