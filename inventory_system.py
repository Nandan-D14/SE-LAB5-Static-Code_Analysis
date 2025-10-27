"""Inventory management system module."""
import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add item to inventory."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove item from inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except (KeyError, ValueError):
        pass


def get_qty(item):
    """Get quantity of item."""
    return stock_data[item]


def load_data(file="inventory.json"):
    """Load data from file."""
    with open(file, "r", encoding='utf-8') as f:
        global stock_data
        stock_data = json.loads(f.read())


def save_data(file="inventory.json"):
    """Save data to file."""
    with open(file, "w", encoding='utf-8') as f:
        f.write(json.dumps(stock_data))


def print_data():
    """Print inventory data."""
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def check_low_items(threshold=5):
    """Check for low stock items."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Main function."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print('eval used')  # removed dangerous eval


main()
