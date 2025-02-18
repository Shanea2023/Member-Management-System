import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('members.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the members table
cursor.execute('''
CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    date_of_birth TEXT NOT NULL,
    email TEXT NOT NULL,
    membership_type TEXT NOT NULL,
    start_date TEXT NOT NULL,
    status TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")