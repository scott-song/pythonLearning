# Python Learning Project Makefile

# Variables
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Default target
.DEFAULT_GOAL := help

# Create virtual environment
venv:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip

# Install dependencies
install: venv
	$(PIP) install -r requirements.txt

# Run main application
run:
	$(PYTHON) src/main.py

# Watch for changes and auto-run
watch:
	$(PYTHON) scripts/watch.py

# Run tests
test:
	$(PYTHON) -m pytest tests/ -v

# Format code
format:
	$(PYTHON) -m black src/ tests/ scripts/

# Check code style
lint:
	$(PYTHON) -m flake8 src/ tests/ scripts/

# Check specific file
lint-file:
	$(PYTHON) -m flake8 $(FILE)

# Show flake8 version and plugins
lint-info:
	$(PYTHON) -m flake8 --version

# Type checking
typecheck:
	$(PYTHON) -m mypy src/ scripts/

# Markdown formatting and linting
format-md:
	$(PYTHON) -m mdformat *.md --wrap 100

# Check markdown formatting
check-md:
	$(PYTHON) -m mdformat --check *.md --wrap 100

# Clean up
clean:
	rm -rf $(VENV)
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

# Development setup (install + format + test)
dev: install format test

# Help
help:
	@echo "Available targets:"
	@echo "  venv      - Create virtual environment"
	@echo "  install   - Install dependencies"
	@echo "  run       - Run the main application"
	@echo "  test      - Run tests"
	@echo "  format    - Format code with black"
	@echo "  lint      - Check code style with flake8"
	@echo "  lint-file - Check specific file (usage: make lint-file FILE=path/to/file.py)"
	@echo "  lint-info - Show flake8 version and available plugins"
	@echo "  typecheck - Run type checking with mypy"
	@echo "  format-md - Format markdown files"
	@echo "  check-md  - Check markdown formatting"
	@echo "  dev       - Complete development setup"
	@echo "  clean     - Clean up generated files"
	@echo "  help      - Show this help message"

.PHONY: venv install run test format lint typecheck clean dev help
