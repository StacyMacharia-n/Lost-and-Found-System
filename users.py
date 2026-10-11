from database import connect_db


def register_user():
    print("\n===== USER REGISTRATION =====")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Create a password: ")

    connection = connect_db()
    cursor = connection.cursor()

    
    try:
        cursor.execute("""
            INSERT INTO users (name, email, password, role)
            VALUES (?, ?, ?, ?)
        """, (name, email, password, "USER"))

        connection.commit()
        print("\nRegistration successful! 🎉")

    except Exception as error:
        print(f"\nRegistration error: {error}")

    finally:
        connection.close()


def login_user():
    print("\n===== USER LOGIN =====")

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, role
        FROM users
        WHERE email = ? AND password = ?
    """, (email, password))

    user = cursor.fetchone()
    connection.close()

    if user:
        print(f"\nWelcome, {user[1]}! 👋")
        return user
    else:
        print("\nInvalid email or password.")
        return None