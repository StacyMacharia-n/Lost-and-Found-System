from database import connect_db
from notifications import create_notification


def calculate_match_score(lost_item, found_item):
    score = 0

    # Compare item name
    if lost_item[1].lower() == found_item[1].lower():
        score += 30

    # Compare category
    if lost_item[2].lower() == found_item[2].lower():
        score += 20

    # Compare colour
    if lost_item[3].lower() == found_item[3].lower():
        score += 15

    # Compare location
    if lost_item[4].lower() == found_item[4].lower():
        score += 20

    # Compare description
    lost_description = lost_item[6].lower()
    found_description = found_item[6].lower()

    lost_words = set(lost_description.split())
    found_words = set(found_description.split())

    common_words = lost_words.intersection(found_words)

    if common_words:
        score += 15

    return score


def find_matches():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM lost_items
        WHERE status = 'LOST'
    """)

    lost_items = cursor.fetchall()

    cursor.execute("""
        SELECT * FROM found_items
        WHERE status = 'FOUND'
    """)

    found_items = cursor.fetchall()

    connection.close()

    if not lost_items:
        print("\nNo lost items available.")
        return

    if not found_items:
        print("\nNo found items available.")
        return

    print("\n===== SMART ITEM MATCHING =====")

    for lost_item in lost_items:

        print(f"\nLost Item: {lost_item[1]}")

        best_score = 0
        best_match = None

        for found_item in found_items:

            score = calculate_match_score(lost_item, found_item)

            if score > best_score:
                best_score = score
                best_match = found_item

        if best_match:
            print(f"Found Item: {best_match[1]}")
            print(f"Match Score: {best_score}%")

         
            if best_score >= 70:
                print("Status: STRONG MATCH")

                user_id = lost_item[8]

                create_notification(
                    user_id,
                    f"Strong match found for your lost item: "
                    f"{lost_item[1]}. Found item: {best_match[1]}. "
                    f"Match score: {best_score}%."
                )

                print("Notification created for the reporting user.")

            elif best_score >= 40:
                print("Status: POSSIBLE MATCH")
            else:
                print("Status: LOW MATCH")   