"""Inventory management system module."""
import json
from datetime import datetime


def add_item(stock_data, item="default", qty=0, logs=None):
    """Add item to inventory."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(stock_data, item, qty):
    """Remove item from inventory."""
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        return
    if item in stock_data:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]


def get_qty(stock_data, item):
    """Get quantity of item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load data from file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_data(stock_data, file="inventory.json"):
    """Save data to file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data(stock_data):
    """Print inventory data."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(stock_data, threshold=5):
    """Check for low stock items."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function."""
    stock_data = {}
    logs = []

    add_item(stock_data, "apple", 10, logs)
    add_item(stock_data, "banana", -2, logs)
    add_item(stock_data, 123, "ten", logs)  # ignored invalid types
    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)

    print("Apple stock:", get_qty(stock_data, "apple"))
    print("Low items:", check_low_items(stock_data))

    save_data(stock_data)
    stock_data = load_data()
    print_data(stock_data)


if __name__ == "__main__":
    main()
