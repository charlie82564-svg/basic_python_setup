# Python Scripting Setup Guide

A beginner-friendly repository to get started with Python scripting and virtual environments.

## Quick Start

### 1. Virtual Environment Setup
```bash
# Virtual environment already created in .venv/
# Activate it:
source .venv/bin/activate


# Install packages:
pip install -r requirements.txt
```

### 2. Run Example Scripts
```bash
# Simple greeting script:
python scripts/hello.py

# Data manipulation example:
python scripts/data_example.py
```

### 3. Deactivate When Done
```bash
deactivate
```

## What's Included

**Essential Packages** (in `requirements.txt`):
- `requests` - Make HTTP requests and work with APIs
- `pandas` - Data analysis and manipulation
- `python-dotenv` - Manage environment variables
- `pytest` - Write and run tests
- `black` - Auto-format your code
- `flake8` - Check code quality

## Recommended VS Code Extensions

Install these for the best Python development experience:
- **Python** (ms-python.python) - Official Python support
- **Pylance** (ms-python.vscode-pylance) - Fast language server
- **Black Formatter** (ms-python.black-formatter) - Auto-formatting
- **autoDocstring** (njpwerner.autodocstring) - Generate docstrings
- **Error Lens** (usernamehm.errorlens) - Inline error highlighting

## Learning Resources

**Documentation:**
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python Tutorials](https://realpython.com/)
- [Python Package Index (PyPI)](https://pypi.org/)

**Practice:**
- [Exercism Python Track](https://exercism.org/tracks/python)
- [LeetCode](https://leetcode.com/) - Algorithm practice
- [HackerRank Python](https://www.hackerrank.com/domains/python)

**Quick Reference:**
- [Python Cheat Sheet](https://www.pythoncheatsheet.org/)
- [PEP 8 Style Guide](https://pep8.org/)

## Tips

- Always activate your virtual environment before working
- Use `pip list` to see installed packages
- Run `black .` to auto-format all Python files
- Run `flake8 .` to check code quality
- Add secrets to `.env` file (never commit this!)

## Project Structure
```
basic_python_setup/
├── .venv/              # Virtual environment (don't commit)
├── scripts/            # Your Python scripts go here
│   ├── hello.py        # Simple example script
│   └── data_example.py # Pandas example
├── requirements.txt    # Package dependencies
├── .gitignore         # Files to exclude from git
└── README.md          # This file
```