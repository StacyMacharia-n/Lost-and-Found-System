from database import connect_db
from datetime import datetime


def report_lost_item(user_id):
    print("\n===== REPORT A LOST ITEM =====")

    item_name = input("Enter item name: ")
    category = input("Enter category: ")
    colour = input("Enter colour: ")
    location = input("Where was the item lost? ")
    date_lost = input("Enter date lost (YYYY-MM-DD): ")
    description = input("Describe the item: ")

    print("\nUrgency Level")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    urgency_choice = input("Choose urgency: ")

    if urgency_choice == "1":
        urgency = "LOW"
    elif urgency_choice == "2":
        urgency = "MEDIUM"
    elif urgency_choice == "3":
        urgency = "HIGH"
    else:
        urgency = "MEDIUM"

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO lost_items
        (item_name, category, colour, location, date_lost, description, status, user_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        item_name,
        category,
        colour,
        location,
        date_lost,
        description,
        "LOST",
        user_id
    ))

    connection.commit()

    item_id = cursor.lastrowid

    connection.close()

    unique_id = f"LF-{datetime.now().year}-{item_id:04d}"

    print("\n================================")
    print("Lost item reported successfully!")
    print(f"Your Lost Item ID is: {unique_id}")
    print(f"Status: LOST")
    print(f"Urgency: {urgency}")
    print("================================")