
from database import connect_db


def view_lost_items():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, item_name, category, colour, location,
               date_lost, status, urgency
        FROM lost_items
    """)

    items = cursor.fetchall()
    connection.close()

    print("\n===== ALL LOST ITEMS =====")

    if not items:
        print("No lost items have been reported.")
        return

    for item in items:
        item_code = f"LF-{__import__('datetime').datetime.now().year}-{item[0]:04d}"
        print("-" * 35)
        print(f"Item ID: {item_code}")
        print(f"Name: {item[1]}")
        print(f"Category: {item[2]}")
        print(f"Colour: {item[3]}")
        print(f"Location: {item[4]}")
        print(f"Date lost: {item[5]}")
        print(f"Status: {item[6]}")
        print(f"Urgency: {item[7]}")


def view_found_items():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, item_name, category, colour, location,
               date_found, status
        FROM found_items
    """)

    items = cursor.fetchall()
    connection.close()

    print("\n===== ALL FOUND ITEMS =====")

    if not items:
        print("No found items have been reported.")
        return

    for item in items:
        item_code = f"FD-{__import__('datetime').datetime.now().year}-{item[0]:04d}"
        print("-" * 35)
        print(f"Item ID: {item_code}")
        print(f"Name: {item[1]}")
        print(f"Category: {item[2]}")
        print(f"Colour: {item[3]}")
        print(f"Location: {item[4]}")
        print(f"Date found: {item[5]}")
        print(f"Status: {item[6]}")


def search_items():
    search_term = input(
        "\nEnter item name, category, colour, or location to search: "
    ).strip()

    if not search_term:
        print("Please enter a search term.")
        return

    connection = connect_db()
    cursor = connection.cursor()
    pattern = f"%{search_term}%"

    cursor.execute("""
        SELECT id, item_name, category, colour, location,
               date_lost, status
        FROM lost_items
        WHERE item_name LIKE ? OR category LIKE ?
           OR colour LIKE ? OR location LIKE ?
    """, (pattern, pattern, pattern, pattern))

    lost_items = cursor.fetchall()

    cursor.execute("""
        SELECT id, item_name, category, colour, location,
               date_found, status
        FROM found_items
        WHERE item_name LIKE ? OR category LIKE ?
           OR colour LIKE ? OR location LIKE ?
    """, (pattern, pattern, pattern, pattern))

    found_items = cursor.fetchall()
    connection.close()

    print("\n===== SEARCH RESULTS =====")

    if not lost_items and not found_items:
        print("No matching items found.")
        return

    for item in lost_items:
        print(
            f"LOST | LF-{__import__('datetime').datetime.now().year}-{item[0]:04d} "
            f"| {item[1]} | {item[2]} | {item[3]} | "
            f"{item[4]} | Status: {item[6]}"
        )

    for item in found_items:
        print(
            f"FOUND | FD-{__import__('datetime').datetime.now().year}-{item[0]:04d} "
            f"| {item[1]} | {item[2]} | {item[3]} | "
            f"{item[4]} | Status: {item[6]}"
        )