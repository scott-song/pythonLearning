# Python Learning Project

A comprehensive Python 3.12+ learning project with practical demonstrations of core Python concepts,
advanced features, and best practices. This project is designed for developers who want to learn
Python through hands-on examples and real-world patterns.

## 🚀 Features

### Core Learning Modules

- **🛠️ Exception Handling**: Comprehensive error and exception handling patterns
- **🧮 Concurrency**: Threading, asyncio, multiprocessing, and concurrent.futures
- **🏗️ Object-Oriented Programming**: Classes, inheritance, dataclasses, and special methods
- **📁 Input/Output Operations**: File handling, JSON, CLI arguments, and path operations
- **🔄 Control Flow**: Loops, conditionals, and flow control patterns
- **📊 Data Structures**: Lists, dictionaries, sets, and advanced data manipulation
- **🎯 Functions**: Function definitions, decorators, lambdas, and functional programming

### Development Tools

- **🔍 Auto-reload**: File watching with automatic application restart
- **✅ Code Quality**: Black formatting, Flake8 linting, MyPy type checking
- **🧪 Testing**: Pytest framework integration
- **📋 Pre-commit Hooks**: Automated code quality checks

## 📋 Requirements

- **Python 3.12+** (recommended)
- Virtual environment support

## 🛠️ Setup

1. **Clone and navigate to the project:**

   ```bash
   git clone <repository-url>
   cd pythonLearning
   ```

1. **Create a virtual environment:**

   ```bash
   python3.12 -m venv venv
   # or if python3.12 is your default:
   python3 -m venv venv
   ```

1. **Activate the virtual environment:**

   ```bash
   source venv/bin/activate  # On macOS/Linux
   # or on Windows:
   # venv\Scripts\activate
   ```

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

1. **Install pre-commit hooks (optional but recommended):**

   ```bash
   pre-commit install
   ```

## 🎯 Usage

### Run the Main Application

```bash
python src/main.py
```

This will execute all learning demonstrations in sequence:

- Exception handling patterns
- Concurrency examples
- Object-oriented programming concepts

### Development with Auto-reload

For development with automatic file watching and reloading:

```bash
python watch.py
```

This will:

- Run the application once at startup
- Watch for file changes
- Automatically re-run the application when files are modified

### Run Specific Modules

You can also run individual demonstration modules:

```bash
# Exception handling only
python -c "from src.errorException import demo_error_exception; demo_error_exception()"

# Concurrency only
python -c "from src.concurrency import demo_concurrency; demo_concurrency()"

# Classes only
python -c "from src.classes import demo_classes; demo_classes()"

# Input/Output only
python -c "from src.inputOutput import demo_input_output; demo_input_output()"
```

## 📁 Project Structure

```
pythonLearning/
├── src/                           # Source code
│   ├── errorException/            # Exception handling demonstrations
│   │   ├── basic_exceptions.py    # Basic try/except patterns
│   │   ├── custom_exceptions.py   # Custom exception classes
│   │   ├── exception_chaining.py  # Exception chaining and context
│   │   ├── context_managers.py    # Context managers and resource handling
│   │   ├── logging_exceptions.py  # Exception logging patterns
│   │   └── best_practices.py      # Production-ready patterns
│   ├── concurrency/               # Concurrency demonstrations
│   │   ├── threading_demo.py      # Threading patterns and synchronization
│   │   ├── asyncio_demo.py        # Async/await and asyncio patterns
│   │   ├── multiprocessing_demo.py # Multiprocessing and shared memory
│   │   └── concurrent_futures_demo.py # ThreadPoolExecutor and ProcessPoolExecutor
│   ├── classes/                   # Object-oriented programming
│   │   ├── basic_classes.py       # Basic class definitions
│   │   ├── inheritance.py         # Inheritance patterns
│   │   ├── dataclasses_demo.py    # Dataclasses and modern Python
│   │   ├── special_methods.py     # Magic methods and protocols
│   │   ├── advanced_features.py   # Decorators, properties, descriptors
│   │   └── iterators_generators.py # Iterators and generators
│   ├── inputOutput/               # Input/Output operations
│   │   ├── basic_io.py            # Basic input/output patterns
│   │   ├── file_operations.py     # File handling and manipulation
│   │   ├── json_operations.py     # JSON processing
│   │   ├── path_operations.py     # Path and filesystem operations
│   │   ├── cli_operations.py      # Command-line argument handling
│   │   └── utils.py               # I/O utility functions
│   ├── main.py                    # Main application entry point
│   ├── function.py                # Function demonstrations
│   ├── flow.py                    # Control flow patterns
│   ├── list.py                    # List operations and comprehensions
│   ├── text.py                    # String manipulation
│   ├── lamb.py                    # Lambda functions
│   └── dataStructure.py           # Data structure demonstrations
├── tests/                         # Test files
├── scripts/                       # Utility scripts
├── watch.py                       # Auto-reload development server
├── requirements.txt               # Python dependencies
├── pyproject.toml                 # Project configuration
├── setup.cfg                      # Setup configuration
├── Makefile                       # Build automation
├── .pre-commit-config.yaml        # Pre-commit hooks configuration
├── .flake8                        # Flake8 linting configuration
├── .gitignore                     # Git ignore patterns
└── README.md                      # This file
```

## 🧪 Testing

Run tests using pytest:

```bash
pytest tests/
```

Run tests with coverage:

```bash
pytest --cov=src tests/
```

## 🔧 Development

### Code Quality

This project uses several tools to maintain code quality:

- **Black**: Code formatting
- **Flake8**: Linting and style checking
- **MyPy**: Type checking
- **Pre-commit**: Automated quality checks

Run quality checks manually:

```bash
# Format code
black src/

# Lint code
flake8 src/

# Type check
mypy src/

# Run all pre-commit hooks
pre-commit run --all-files
```

### Adding New Modules

1. Create your Python module in the appropriate `src/` subdirectory
1. Add comprehensive docstrings and type hints
1. Create a demo function following the existing patterns
1. Add tests in the `tests/` directory
1. Update imports in the relevant `__init__.py` file

### Dependencies

Current dependencies include:

- **Core**: `requests`, `python-dotenv`, `watchdog`
- **Development**: `pytest`, `black`, `flake8`, `mypy`, `pre-commit`
- **Documentation**: `mdformat`

Add new dependencies to `requirements.txt` and run:

```bash
pip install -r requirements.txt
```

## 📚 Learning Objectives

This project demonstrates:

- **Exception Handling**: Proper error handling, custom exceptions, logging
- **Concurrency**: Threading, async programming, multiprocessing
- **OOP**: Classes, inheritance, composition, design patterns
- **I/O Operations**: File handling, JSON, CLI interfaces
- **Python Best Practices**: Type hints, documentation, testing
- **Development Workflow**: Linting, formatting, pre-commit hooks

## 🤝 Contributing

1. Fork the repository
1. Create a feature branch
1. Make your changes following the existing patterns
1. Ensure all tests pass and code quality checks succeed
1. Submit a pull request

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed for learning Python.

______________________________________________________________________

**Happy Python Learning! 🐍**
