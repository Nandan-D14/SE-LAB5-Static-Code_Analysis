# SE-LAB5-Static-Code_Analysis

This project is a simple inventory management system used to demonstrate static code analysis in Python.

## Features

- Add items to the inventory.
- Remove items from the inventory.
- Get the quantity of an item.
- Check for low stock items.
- Save inventory data to a JSON file.
- Load inventory data from a JSON file.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Nandan-D14/SE-LAB5-Static-Code_Analysis.git
    ```
2.  Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
3.  Activate the virtual environment:
    -   Windows:
        ```bash
        .venv\Scripts\activate
        ```
    -   macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```
4.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the inventory system, execute the following command:

```bash
python inventory_system.py
```

## Static Analysis Tools

This project uses the following static analysis tools:

-   **pylint**: A tool for finding errors, enforcing a coding standard, and looking for code smells.
-   **bandit**: A tool designed to find common security issues in Python code.
-   **flake8**: A tool to check your Python code against some of the style conventions in PEP 8.

The reports from these tools can be found in the `Lab5` directory.

# Issues Documentation Table

Based on the static analysis reports from Pylint, Bandit, and Flake8, here are the identified issues and fixes:

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|-------------|
| **Mutable default argument** | Bug | 6 | `logs=[]` shared across function calls, causing unexpected behavior | Changed to `logs=None` and initialize list inside function |
| **Bare except clause** | Security | 16 | Catching all exceptions silently, hiding potential errors | Replaced with specific exception types `(KeyError, ValueError)` |
| **Use of eval()** | Security | 50 | Dangerous code execution vulnerability allowing arbitrary code execution | Removed eval and used direct `print()` statement |
| **Global variable usage** | Design | Multiple | Using global `stock_data` variable across all functions | Restructured to pass `stock_data` as parameter to all functions |
| **Missing input validation** | Quality | 44 | No type checking for function parameters, allowing invalid data | Added `isinstance()` checks for parameter validation |
| **Poor file handling** | Security | 22, 28 | Files opened without context managers, potential resource leaks | Used `with` statements for automatic file closing |
| **Missing encoding specification** | Security | File ops | Files opened without specified encoding, potential encoding issues | Added `encoding="utf-8"` to all file operations |
| **Unused imports** | Quality | 2 | `logging` imported but never used in the code | Removed unused import statement |
| **Missing docstrings** | Quality | Multiple | Module and functions missing documentation | Added comprehensive docstrings to module and all functions |
| **Inconsistent naming** | Style | Multiple | Function names using camelCase instead of snake_case | Renamed all functions to follow PEP8 snake_case convention |
| **Poor string formatting** | Style | 10 | Using % formatting instead of modern f-strings | Converted to f-string formatting |
| **No main guard** | Quality | 52 | Script runs on import instead of only when executed directly | Added `if __name__ == "__main__":` guard |

## Key Issues Fixed (Minimum 4 Required):

1. **✅ Mutable default argument** - Fixed potential bug where lists were shared across function calls
2. **✅ Bare except clause** - Improved error handling and security
3. **✅ Use of eval()** - Eliminated major security vulnerability
4. **✅ Global variable usage** - Improved code design and testability
5. **✅ Missing input validation** - Added proper type checking
6. **✅ Poor file handling** - Used context managers for resource safety

## Severity Classification:

- **High Severity**: eval() usage, bare except clauses, mutable default arguments
- **Medium Severity**: Global variable usage, missing input validation
- **Low Severity**: Style issues, naming conventions, docstrings

The fixes address both immediate functional issues and long-term maintainability concerns, significantly improving the code's security, reliability, and professional quality.
