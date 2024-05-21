from flask import Flask, request
import sqlite3
import random

app = Flask(__name__)

# Function to establish database connection
def get_db_connection():
    conn = sqlite3.connect('npay.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route for registration
@app.route("/registration", methods=["POST"])
def registration():
    try:
        # Connect to database
        conn = get_db_connection()
        # Get data from the request
        data = request.json
        # Extract values from the request data
        organization_name = data.get("organization_name")
        roc = data.get("roc")
        date_of_incorporation = data.get("date_of_incorporation")
        organization_pan = data.get("organization_pan")
        upload_pan = data.get("upload_pan")
        organization_tan = data.get("organization_tan")
        organization_gst = data.get("organization_gst")
        upload_gst = data.get("upload_gst")
        organization_cin = data.get("organization_cin")
        upload_cin = data.get("upload_cin")
        official_email = data.get("official_email")
        official_contact = data.get("official_contact")
        # Insert a record into the database using query parameters
        conn.execute("INSERT INTO registration (organization_name, roc, date_of_incorporation, organization_pan, upload_pan, organization_tan, organization_gst, upload_gst, organization_cin, upload_cin, official_email, official_contact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                     (organization_name, roc, date_of_incorporation, organization_pan, upload_pan, organization_tan, organization_gst, upload_gst, organization_cin, upload_cin, official_email, official_contact))
        # Commit the changes
        conn.commit()
        # Close the connection
        conn.close()
        return {'status': 'success'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

# OTP Sending route   
@app.route("/send_otp", methods=["POST"])
def send_otp():
    email = request.json.get("email")
    # return str(email)
    otp = random.randint(100000, 999999)
    # Insert the otp into the database
    # check email
    conn = get_db_connection()
    conn.execute("INSERT INTO otp (otp, mobile_number) VALUES (?, ?)", (otp, email))
    conn.commit()
    # Send OTP to the user
    return {'status': 'OTP Sent successfully', 'otp': str(otp)}

# OTP Verification route
@app.route("/verify_otp", methods=["POST"])
def verify_otp():
    audit_id = request.json.get("audit_id")
    conn = get_db_connection()
    # Fetch the otp from the database
    cursor = conn.execute("SELECT * FROM otp WHERE id = ? and is_verified = 0", (audit_id,))
    row = cursor.fetchone()
    if row:
        # Update the is_verified flag to True
        conn.execute("UPDATE otp SET is_verified = ? WHERE id = ?", (1, audit_id))
        conn.commit()
        conn.close()
        return {'status': 'OTP Verified successfully'}
    conn.close()  # Don't forget to close the connection
    return {'status': 'OTP Verification failed'}

if __name__ == "__main__":
    app.run()
