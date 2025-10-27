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
