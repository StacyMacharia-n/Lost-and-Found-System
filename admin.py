
from database import connect_db



def admin_dashboard():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM lost_items")
    total_lost = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM found_items")
    total_found = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM claims
        WHERE status = 'PENDING'
    """)
    pending_claims = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM claims
        WHERE status = 'APPROVED'
    """)
    approved_claims = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM claims
        WHERE status = 'REJECTED'
    """)
    rejected_claims = cursor.fetchone()[0]

    connection.close()

    print("\n" + "=" * 42)
    print("           ADMIN DASHBOARD")
    print("=" * 42)
    print(f"Total registered users: {total_users}")
    print(f"Total lost items:       {total_lost}")
    print(f"Total found items:      {total_found}")
    print("-" * 42)
    print(f"Pending claims:         {pending_claims}")
    print(f"Approved claims:        {approved_claims}")
    print(f"Rejected claims:        {rejected_claims}")
    print("=" * 42)

    
def view_pending_claims():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT claims.id,
               found_items.item_name,
               users.name,
               claims.verification_details,
               claims.claim_date
        FROM claims
        JOIN found_items
            ON claims.found_item_id = found_items.id
        JOIN users
            ON claims.user_id = users.id
        WHERE claims.status = 'PENDING'
        ORDER BY claims.id DESC
    """)

    claims = cursor.fetchall()
    connection.close()

    print("\n===== PENDING CLAIMS =====")

    if not claims:
        print("There are no pending claims.")
        return

    for claim in claims:
        print("-" * 40)
        print(f"Claim ID: {claim[0]}")
        print(f"Found Item: {claim[1]}")
        print(f"Claimed By: {claim[2]}")
        print(f"Verification Details: {claim[3]}")
        print(f"Claim Date: {claim[4]}")
        
def review_claim():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, found_item_id, user_id, status
        FROM claims
        WHERE status = 'PENDING'
    """)

    claims = cursor.fetchall()

    if not claims:
        print("\nThere are no pending claims to review.")
        connection.close()
        return

    print("\n===== REVIEW CLAIMS =====")

    for claim in claims:
        print(
            f"Claim ID: {claim[0]} | "
            f"Found Item ID: {claim[1]} | "
            f"User ID: {claim[2]}"
        )

    claim_id = input("\nEnter the Claim ID to review: ")

    if not claim_id.isdigit():
        print("Please enter a valid claim ID.")
        connection.close()
        return

    cursor.execute("""
        SELECT id, found_item_id
        FROM claims
        WHERE id = ? AND status = 'PENDING'
    """, (int(claim_id),))

    claim = cursor.fetchone()

    if not claim:
        print("Pending claim not found.")
        connection.close()
        return

    decision = input("Approve or reject? (A/R): ").strip().upper()

    if decision == "A":
        cursor.execute("""
            UPDATE claims
            SET status = 'APPROVED'
            WHERE id = ?
        """, (claim[0],))

        cursor.execute("""
            UPDATE found_items
            SET status = 'CLAIMED'
            WHERE id = ?
        """, (claim[1],))

        print("Claim approved successfully!")

    elif decision == "R":
        cursor.execute("""
            UPDATE claims
            SET status = 'REJECTED'
            WHERE id = ?
        """, (claim[0],))

        print("Claim rejected.")

    else:
        print("Invalid choice. Enter A or R.")
        connection.close()
        return

    connection.commit()
    connection.close()