import sqlite3

# Replace with your SQLite database file
DATABASE_FILE = "example.db"

try:
    # Connect to the SQLite database
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    print(f"Connected to database: {DATABASE_FILE}\n")

    # SQL query to fetch all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch all results
    tables = cursor.fetchall()

    # Check if tables exist
    if tables:
        print("Tables present in the database:")
        for table in tables:
            print(f"- {table[0]}")
    else:
        print("No tables found in the database.")

except sqlite3.Error as error:
    print("Error while connecting to SQLite:", error)

finally:
    # Close the connection safely
    if 'connection' in locals():
        connection.close()
        print("\nSQLite connection closed.")