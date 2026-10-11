
from admin import admin_dashboard, view_pending_claims, review_claim
from notifications import view_notifications, mark_notification_read
from reports import view_lost_items, view_found_items, search_items
from claims import claim_item
from database import create_tables
from users import register_user, login_user
from Lost_items import report_lost_item
from Found_items import report_found_item
from matching import find_matches
create_tables()

while True:
    print("\n===== LOST & FOUND SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Report Lost Item")
    print("4. Report Found Item")
    print("5. Find Matching Items")
    print("6. Claim Found Item")
    print("7.View Lost Items")
    print("8.View Found Items")
    print("9.Search Items")
    print("10.View Notifications")
    print("11.Mark Notification as Read")
    print("12.Exit")
    print("13.Admin Dashboard")
    print("14. View Pending Claims")
    print("15. Review Claims (Approve/Reject)")
    

    choice = input("Choose an option: ")

    if choice == "1":
        register_user()

    elif choice == "2":
        login_user()

    elif choice == "3":
        user = login_user()

        if user:
            report_lost_item(user[0])

    elif choice == "4":
        user = login_user()

        if user:
            report_found_item(user[0])
    elif choice == "5":  
        find_matches()
        
    
    elif choice == "6":
        user = login_user()

        if user:
            claim_item(user[0])

    elif choice == "7":
        view_lost_items()

    elif choice == "8":
        view_found_items()

    elif choice == "9":
        search_items()

    
    elif choice == "10":
     user = login_user()

     if user:
                view_notifications(user[0])

    
    elif choice == "11":
            user = login_user()
            if user:
                view_notifications(user[0])
                notification_id = input("Enter Notification ID to mark as read: ")

                if notification_id.isdigit():
                    mark_notification_read(user[0], int(notification_id))
                else:
                    print("Please enter a valid notification ID.")


    
    elif choice == "13":
            user = login_user()
            if user:
                if user[2] == "ADMIN":
                    admin_dashboard()
                else:
                    print("Access denied. Admins only.")
    
    elif choice == "14":
            user = login_user()
            if user:
                if user[2].upper() == "ADMIN":
                    view_pending_claims()
                else:
                    print("Access denied. Admins only.")

    elif choice == "15":
            user = login_user()
            if user:
                if user[2].upper() == "ADMIN":
                    review_claim()
                else:
                    print("Access denied. Admins only.")                
    elif choice == "12":
     print("Goodbye!")
    break

    

else:
        print("Invalid choice.")