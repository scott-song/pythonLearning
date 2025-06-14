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
	$(PYTHON) watch.py

# Run tests
test:
	$(PYTHON) -m pytest tests/ -v

# Format code
format:
	$(PYTHON) -m black src/ tests/

# Check code style
lint:
	$(PYTHON) -m flake8 src/ tests/ --max-line-length=88

# Type checking
typecheck:
	$(PYTHON) -m mypy src/

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
	@echo "  typecheck - Run type checking with mypy"
	@echo "  dev       - Complete development setup"
	@echo "  clean     - Clean up generated files"
	@echo "  help      - Show this help message"

.PHONY: venv install run test format lint typecheck clean dev help 