import sqlite3
import os



try:
    # Get the current working directory
    current_directory = os.getcwd()
    # Set the database file path
    db_path = os.path.join(current_directory, 'npay.db')
    
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    print("Database connection successful")

    # Print the absolute path of the database file
    absolute_db_path = os.path.abspath(db_path)
    print(f"Database path: {db_path}")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create a registration table
    cursor.execute('''CREATE TABLE IF NOT EXISTS registration (
                        id INTEGER PRIMARY KEY,
                        organization_name TEXT NOT NULL,
                        roc TEXT NOT NULL,
                        date_of_incorporation DATE NOT NULL,
                        organization_pan TEXT NOT NULL,
                        upload_pan BLOB NOT NULL,
                        organization_tan TEXT NOT NULL,
                        organization_gst TEXT NOT NULL,
                        upload_gst BLOB NOT NULL,
                        organization_cin TEXT NOT NULL,
                        upload_cin BLOB NOT NULL,
                        official_email TEXT NOT NULL,
                        official_contact TEXT NOT NULL
                    )''')
    print("Registration table created successfully")

    # Create an otp table
    cursor.execute('''CREATE TABLE IF NOT EXISTS otp (
                        id INTEGER PRIMARY KEY,
                        otp INTEGER NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        mobile_number TEXT NOT NULL,
                        is_verified BOOLEAN DEFAULT FALSE
                    )''')
    print("OTP table created successfully")

    # Create Invoice Table 
    cursor.execute('''CREATE TABLE IF NOT EXISTS invoice (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        user_id TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        gst REAL NOT NULL,
                        address TEXT NOT NULL,
                        customer_name TEXT NOT NULL,
                        customer_address TEXT NOT NULL,
                        invoice_number TEXT NOT NULL,
                        invoice_date DATE NOT NULL,
                        due_date DATE NOT NULL,
                        discount REAL NOT NULL,
                        terms TEXT NOT NULL,
                        total_amount REAL NOT NULL
                    )''')
    print("Invoice table created successfully")

    # Create Item Table 
    cursor.execute('''CREATE TABLE IF NOT EXISTS item (
                        id INTEGER PRIMARY KEY,
                        invoice_id INTEGER NOT NULL,
                        item TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        hsn_code REAL NOT NULL,
                        price REAL NOT NULL,
                        quantity INTEGER NOT NULL,
                        gst REAL NOT NULL,
                        taxable_amount REAL NOT NULL,
                        total_amount REAL NOT NULL,
                        FOREIGN KEY (invoice_id) REFERENCES invoice(id)
                    )''')
    print("Item table created successfully")

    # Save (commit) the changes
    conn.commit()
    print("Changes committed to the database")

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    # Close the connection
    if conn:
        conn.close()
        print("SQLite connection is closed")
