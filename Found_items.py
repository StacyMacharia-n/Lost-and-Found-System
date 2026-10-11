from database import connect_db
from datetime import datetime


def report_found_item(user_id):
    print("\n===== REPORT A FOUND ITEM =====")

    item_name = input("Enter item name: ")
    category = input("Enter category: ")
    colour = input("Enter colour: ")
    location = input("Where was the item found? ")
    date_found = input("Enter date found (YYYY-MM-DD): ")
    description = input("Describe the item: ")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO found_items
        (item_name, category, colour, location, date_found, description, status, user_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        item_name,
        category,
        colour,
        location,
        date_found,
        description,
        "FOUND",
        user_id
    ))

    connection.commit()

    item_id = cursor.lastrowid

    connection.close()

    unique_id = f"FD-{datetime.now().year}-{item_id:04d}"

    print("\n================================")
    print("Found item reported successfully!")
    print(f"Your Found Item ID is: {unique_id}")
    print("Status: FOUND")
    print("================================")