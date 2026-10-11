
from database import connect_db


def claim_item(user_id):
    print("\n===== CLAIM A FOUND ITEM =====")

    found_id = input(
        "Enter the Found Item ID (e.g. FD-2026-0001): "
    )

    # Extract the database ID from the Found Item ID
    try:
        database_id = int(found_id.split("-")[-1])
    except ValueError:
        print("Invalid Found Item ID format.")
        return

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, item_name, colour, location, status
        FROM found_items
        WHERE id = ?
    """, (database_id,))

    item = cursor.fetchone()

    if not item:
        print("Found item not found.")
        connection.close()
        return

    print(f"\nItem: {item[1]}")
    print(f"Colour: {item[2]}")
    print(f"Location: {item[3]}")
    print(f"Status: {item[4]}")

    if item[4] != "FOUND":
        print("This item is not available for claiming.")
        connection.close()
        return

    if item[0] and user_id:
        print("\nPlease provide details to help verify ownership.")
        details = input(
            "Describe a unique feature proving ownership: "
        )

        cursor.execute("""
            INSERT INTO claims
            (found_item_id, user_id, verification_details, status)
            VALUES (?, ?, ?, ?)
        """, (item[0], user_id, details, "PENDING"))

        connection.commit()

        print("\nClaim submitted successfully!")
        print(f"Item: {item[1]}")
        print("Claim status: PENDING")
        print("An administrator must verify your claim.")
    connection.close()

