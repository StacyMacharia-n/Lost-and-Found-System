# Lost and Found Management System

A Python-based Lost and Found Management System designed to help users report lost items, register found items, search for potential matches, and manage the process of reclaiming lost belongings.

## About the Project

Losing personal belongings can be stressful, especially when there is no organized way to report missing items or connect people with items that have been found. This project provides a simple, menu-driven system that helps users manage lost and found reports in one place.

The system includes user registration and login, lost and found item reporting, smart item matching, claim management, notifications, and administrative review of claims.

## Features

- **User Registration and Login:** Allows users to create accounts and log in.
- **Report Lost Items:** Enables users to submit details about missing belongings.
- **Report Found Items:** Allows users to record items they have found.
- **Smart Item Matching:** Helps identify potential matches between lost and found reports.
- **Item Search:** Supports searching for reported items.
- **Claim Found Items:** Allows users to submit claims for found belongings.
- **Notifications:** Provides a way to view notifications and mark them as read.
- **Admin Dashboard:** Provides administrative functions for managing the system.
- **Claim Review:** Allows administrators to review claims and approve or reject them.
- **Database Management:** Uses SQLite to store application data locally.

## Technologies Used

- **Programming Language:** Python
- **Database:** SQLite
- **Development Environment:** Visual Studio Code
- **Version Control:** Git
- **Repository Hosting:** GitHub

## Project Structure

```text
Lost-and-Found-System/
├── main.py
├── users.py
├── database.py
├── Lost_items.py
├── Found_items.py
├── matching.py
├── claims.py
├── notifications.py
├── reports.py
├── admin.py
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

Before running the project, install:

- Python 3
- Visual Studio Code (recommended)

SQLite is supported through Python's built-in `sqlite3` module, so a separate SQLite installation may not be necessary.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/StacyMacharia-n/Lost-and-Found-System.git
   ```

2. Open the project folder:

   ```bash
   cd Lost-and-Found-System
   ```

3. Run the application:

   ```bash
   python main.py
   ```

   On some Windows installations, you may need to use:

   ```bash
   py main.py
   ```

4. Follow the on-screen menu to register, log in, report items, search for matches, and access other available functions.

## How to Use the System

1. Register a user account.
2. Log in using your account details.
3. Report a lost item or a found item.
4. Search for items or use the matching feature to identify possible matches.
5. Submit a claim when a found item appears to belong to you.
6. Check notifications for updates.
7. An administrator can review pending claims and approve or reject them.

The available functions depend on the options implemented in the application.

## Database and Security

The application uses SQLite for local data storage. The database file is excluded from version control through `.gitignore` to help prevent local user records and claim information from being uploaded accidentally.

**Security note:** For real-world deployment, passwords should be securely hashed, user inputs validated, and administrative access protected. Do not commit real user information, passwords, or private database files to a public repository.

## Future Improvements

Potential future enhancements include:

- Improved matching using item descriptions, categories, locations, and dates.
- Email or SMS notifications.
- Image uploads for lost and found items.
- A graphical user interface or web interface.
- Advanced search and filtering.
- Detailed reports and statistics.
- Stronger authentication and role-based access control.

## Contributing

Suggestions and improvements are welcome. If you would like to contribute, fork the repository, create a branch, make your changes, and submit a pull request.

## Author

**Stacy Macharia**

GitHub: [StacyMacharia-n](https://github.com/StacyMacharia-n)

## License

No license has been specified yet. If you intend to let other people reuse, modify, or distribute this project, consider adding an appropriate open-source license.
