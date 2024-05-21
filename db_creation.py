import sqlite3
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('npay.db')
# Create a cursor object to execute SQL queries
cursor = conn.cursor()
# Create a registration table
cursor.execute('''CREATE TABLE IF NOT EXISTS registration (
                    id INTEGER PRIMARY KEY,
                    organization_name TEXT NOT NULL,
                    roc TEXT NOT NULL,
                    date_of_incorporation DATE NOT NULL,
                    organization_pan TEXT NOT NULL,
                    upload_pan IMAGE NOT NULL,
                    organization_tan TEXT NOT NULL,
                    organization_gst TEXT NOT NULL,
                    upload_gst IMAGE NOT NULL,
                    organization_cin TEXT NOT NULL,
                    upload_cin IMAGE NOT NULL,
                    official_email TEXT NOT NULL,
                    official_contact NUMBER NOT NULL
                )''')
# create a otp table
cursor.execute('''CREATE TABLE IF NOT EXISTS otp (
                    id INTEGER PRIMARY KEY,
                    otp NUMBER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    mobile_number NUMBER NOT NULL,
                    is_verified BOOLEAN DEFAULT FALSE
                )''')

# Save (commit) the changes
conn.commit()
# Close the connection
conn.close()
