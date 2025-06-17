"""Input/Output sub-package for Python learning demonstrations."""

from .basic_io import demo_basic_input, demo_string_formatting
from .cli_operations import demo_command_line_args
from .file_operations import demo_advanced_io, demo_file_operations
from .json_operations import demo_json_operations
from .path_operations import demo_path_operations
from .utils import create_sample_config, read_config_file, write_log_entry

__version__ = "0.1.0"

__all__ = [
    "demo_basic_input",
    "demo_string_formatting",
    "demo_file_operations",
    "demo_json_operations",
    "demo_path_operations",
    "demo_command_line_args",
    "demo_advanced_io",
    "read_config_file",
    "write_log_entry",
    "create_sample_config",
    "demo_input_output",
]


def demo_input_output() -> None:
    """Demonstrate various input/output operations in Python."""
    print("=== Input/Output Demonstrations ===")
    demo_basic_input()
    demo_string_formatting()
    demo_file_operations()
    demo_json_operations()
    demo_path_operations()
    demo_command_line_args()
    demo_advanced_io()
