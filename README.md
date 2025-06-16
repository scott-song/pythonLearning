# Python Learning Project

A Python project set up for learning and development.

**Python Version:** 3.12+ (recommended)

## Setup

1. Create a virtual environment:

   ```bash
   python3.12 -m venv venv
   # or if python3.12 is your default:
   python3 -m venv venv
   ```

1. Activate the virtual environment:

   ```bash
   source venv/bin/activate  # On macOS/Linux
   ```

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script:

```bash
python src/main.py
```

## Project Structure

```
pythonLearning/
├── src/                 # Source code
├── tests/              # Test files
├── requirements.txt    # Project dependencies
├── .gitignore         # Git ignore file
├── .env.example       # Environment variables example
└── README.md          # This file
```

## Development

- Add your Python modules in the `src/` directory
- Write tests in the `tests/` directory
- Update `requirements.txt` when adding new dependencies
