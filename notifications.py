
from database import connect_db


def create_notification(user_id, message):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO notifications (user_id, message, status)
        VALUES (?, ?, 'UNREAD')
    """, (user_id, message))

    connection.commit()
    connection.close()


def view_notifications(user_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, message, status, created_at
        FROM notifications
        WHERE user_id = ?
        ORDER BY id DESC
    """, (user_id,))

    notifications = cursor.fetchall()
    connection.close()

    print("\n===== YOUR NOTIFICATIONS =====")

    if not notifications:
        print("You have no notifications.")
        return

    for notification in notifications:
        print("-" * 35)
        print(f"Notification ID: {notification[0]}")
        print(f"Message: {notification[1]}")
        print(f"Status: {notification[2]}")
        print(f"Date: {notification[3]}")


def mark_notification_read(user_id, notification_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE notifications
        SET status = 'READ'
        WHERE id = ? AND user_id = ?
    """, (notification_id, user_id))

    connection.commit()

    if cursor.rowcount > 0:
        print("Notification marked as read.")
    else:
        print("Notification not found.")

    connection.close()