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

## Summary of Issues Fixed

| Issue Category | Issue | Resolution |
| :--- | :--- | :--- |
| **Code Style & Readability** | Inconsistent function naming (`camelCase`) | Renamed functions to `snake_case` (e.g., `addItem` to `add_item`) to adhere to PEP 8. |
| | Missing docstrings | Added docstrings to the module and all functions to explain their purpose. |
| | Unused import (`logging`) | Removed the unused import statement. |
| | Inefficient string formatting | Replaced older string formatting with f-strings for better readability. |
| | Verbose list creation | Replaced a for loop with a more concise list comprehension in `check_low_items`. |
| **Error Handling & Robustness** | Dangerous default value (`[]`) | Replaced the mutable default argument with `None` in `add_item` to prevent unexpected behavior. |
| | Lack of input validation | Added type checks for arguments in `add_item` and `remove_item`. |
| | Bare `except:` clause | Replaced the bare `except` with specific exception handling (`KeyError`, `ValueError`) in `remove_item`. |
| | No error handling for file operations | Added `try...except` blocks in `load_data` to handle `FileNotFoundError` and `json.JSONDecodeError`. |
| | Unsafe dictionary access | Used the `.get()` method for safer dictionary access in `get_qty`. |
| **Security** | Use of `eval()` | Removed the dangerous `eval()` function call and replaced it with a simple `print`. |
| **Modularity & Design** | Use of global variables | Eliminated the global `stock_data` variable by passing it as a parameter to functions, improving modularity. |
| | Lack of script entry point | Added `if __name__ == "__main__"` to make the script importable as a module. |
| | No use of `with` for file handling | Used the `with` statement for file operations to ensure proper resource management. |