import sqlite3

# Connect to the database file
connection = sqlite3.connect("civiq.db")
cursor = connection.cursor()

# Ask for a list of all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("--- Current Database Tables ---")
for table in tables:
    print(f"📄 {table[0]}")

connection.close()