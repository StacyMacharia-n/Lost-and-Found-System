import sqlite3

def connect_db():
    return sqlite3.connect("lost_found.db")


def create_tables():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lost_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            category TEXT,
            colour TEXT,
            location TEXT,
            date_lost TEXT,
            description TEXT,
            status TEXT DEFAULT 'LOST',
            urgencyTEXT DEFAULT 'MEDIUM',
            user_id INTEGER
        )
    """)
    
   

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS found_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            category TEXT,
            colour TEXT,
            location TEXT,
            date_found TEXT,
            description TEXT,
            status TEXT DEFAULT 'FOUND',
            user_id INTEGER
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS claims (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            found_item_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            verification_details TEXT NOT NULL,
            status TEXT DEFAULT 'PENDING',
            claim_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            message TEXT NOT NULL,
            status TEXT DEFAULT 'UNREAD',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()

    print("Database created successfully!")


if __name__ == "__main__":
    create_tables()