# from flask import Flask, request, jsonify
# import sqlite3
# import random
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///npay.db'
# db = SQLAlchemy(app)

# # # Function to establish database connection
# # def get_db_connection():
# #     conn = sqlite3.connect('npay.db')
# #     conn.row_factory = sqlite3.Row
# #     return conn

# # Route for registration
# @app.route("/registration", methods=["POST"])
# def registration():
#     try:
#         # Connect to database
#         conn = get_db_connection()
#         # Get data from the request
#         data = request.json
#         # Extract values from the request data
#         organization_name = data.get("organization_name")
#         roc = data.get("roc")
#         date_of_incorporation = data.get("date_of_incorporation")
#         organization_pan = data.get("organization_pan")
#         upload_pan = data.get("upload_pan")
#         organization_tan = data.get("organization_tan")
#         organization_gst = data.get("organization_gst")
#         upload_gst = data.get("upload_gst")
#         organization_cin = data.get("organization_cin")
#         upload_cin = data.get("upload_cin")
#         official_email = data.get("official_email")
#         official_contact = data.get("official_contact")
#         # Insert a record into the database using query parameters
#         conn.execute("INSERT INTO registration (organization_name, roc, date_of_incorporation, organization_pan, upload_pan, organization_tan, organization_gst, upload_gst, organization_cin, upload_cin, official_email, official_contact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
#                      (organization_name, roc, date_of_incorporation, organization_pan, upload_pan, organization_tan, organization_gst, upload_gst, organization_cin, upload_cin, official_email, official_contact))
#         # Commit the changes
#         conn.commit()
#         # Close the connection
#         conn.close()
#         return {'status': 'success'}
#     except Exception as e:
#         return {'status': 'error', 'message': str(e)}

# # OTP Sending route   
# @app.route("/send_otp", methods=["POST"])
# def send_otp():
#     email = request.json.get("email")
#     # return str(email)
#     otp = random.randint(100000, 999999)
#     # Insert the otp into the database
#     # check email
#     conn = get_db_connection()
#     conn.execute("INSERT INTO otp (otp, mobile_number) VALUES (?, ?)", (otp, email))
#     conn.commit()
#     # Send OTP to the user
#     return {'status': 'OTP Sent successfully', 'otp': str(otp)}

# # OTP Verification route
# @app.route("/verify_otp", methods=["POST"])
# def verify_otp():
#     audit_id = request.json.get("audit_id")
#     conn = get_db_connection()
#     # Fetch the otp from the database
#     cursor = conn.execute("SELECT * FROM otp WHERE id = ? and is_verified = 0", (audit_id,))
#     row = cursor.fetchone()
#     if row:
#         # Update the is_verified flag to True
#         conn.execute("UPDATE otp SET is_verified = ? WHERE id = ?", (1, audit_id))
#         conn.commit()
#         conn.close()
#         return {'status': 'OTP Verified successfully'}
#     conn.close()  # Don't forget to close the connection
#     return {'status': 'OTP Verification failed'}



# # Invoice model
# class Invoice(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     gst = db.Column(db.String(100), nullable=False)
#     address = db.Column(db.String(200), nullable=False)
#     customer_name = db.Column(db.String(100), nullable=False)
#     customer_address = db.Column(db.String(200), nullable=False)
#     invoice_number = db.Column(db.String(50), nullable=False)
#     invoice_date = db.Column(db.Date, nullable=False)
#     due_date = db.Column(db.Date, nullable=False)
#     discount = db.Column(db.Float, nullable=False)
#     terms = db.Column(db.String(200), nullable=False)
#     total_amount = db.Column(db.Float, nullable=False)

# with app.app_context():
#     db.create_all()

# # Invoice route

# from datetime import datetime

# @app.route("/invoice", methods=["POST"])
# def invoice():
#     try:
#         data = request.json
#         name = data.get("name")
#         gst = data.get("gst")
#         address = data.get("address")
#         customer_name = data.get("customer_name")
#         customer_address = data.get("customer_address")
#         invoice_number = data.get("invoice_number")
#         invoice_date = datetime.strptime(data.get("invoice_date"), "%Y-%m-%d").date()
#         due_date = datetime.strptime(data.get("due_date"), "%Y-%m-%d").date()
#         discount = data.get("discount")
#         terms = data.get("terms")
#         total_amount = data.get("total_amount")

#         invoice = Invoice(name=name, gst=gst, address=address, customer_name=customer_name,
#                            customer_address=customer_address, invoice_number=invoice_number,
#                            invoice_date=invoice_date, due_date=due_date, discount=discount,
#                            terms=terms, total_amount=total_amount)

#         db.session.add(invoice)
#         db.session.commit()

#         return {'status': 'success'}
#     except Exception as e:
#         db.session.rollback()
#         return {'status': 'error', 'message': str(e)}
# # @app.route("/invoice", methods=["POST"])
# # def invoice():
# #     try:
# #         conn = get_db_connection()
# #         data = request.json
# #         name = data.get("name")
# #         gst = data.get("gst")
# #         address = data.get("address")
# #         customer_name = data.get("customer_name")
# #         customer_address = data.get("customer_address")
# #         invoice_number = data.get("invoice_number")
# #         invoice_date = data.get("invoice_date")
# #         due_date = data.get("due_date")
# #         discount = data.get("discount")
# #         terms = data.get("terms")
# #         total_amount = data.get("total_amount")
# #         conn.execute("INSERT INTO invoice (name, gst, address, customer_name, customer_address, invoice_number, invoice_date, due_date, discount, terms, total_amount) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
# #                      (name, gst, address, customer_name, customer_address, invoice_number, invoice_date, due_date, discount, terms, total_amount))
# #         conn.commit()
# #         conn.close()
# #         return {'status': 'success'}
# #     except Exception as e:
# #         return {'status': 'error', 'message': str(e)}
# # get all invoices and id of invoices
# @app.route("/invoice_list", methods=["GET"])
# def get_invoices():
#     invoice_id = request.args.get('id')
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         if invoice_id:
#             cursor.execute("SELECT id, name, gst, address, customer_name, customer_address, invoice_number, invoice_date, due_date, discount, terms, total_amount FROM invoice WHERE id = ?", (invoice_id,))
#             invoice = cursor.fetchone()
#             conn.close()
#             if invoice:
#                 return jsonify({'status': 'success', 'invoice': dict(invoice)})
#             else:
#                 return jsonify({'status': 'error', 'message': 'Invoice not found'})
#         else:
#             cursor.execute("SELECT id, name, gst, address, customer_name, customer_address, invoice_number, invoice_date, due_date, discount, terms, total_amount FROM invoice")
#             invoices = cursor.fetchall()
#             conn.close()
#             return jsonify({'status': 'success', 'invoices': [dict(invoice) for invoice in invoices]})
#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})

# # Create item route
# @app.route("/item", methods=["POST"])
# def item():
#     try:
#         conn = get_db_connection()
#         data = request.json
#         invoice_id = data.get("invoice_id")
#         item = data.get("item")
#         hsn_code = data.get("hsn_code")
#         price = data.get("price")
#         quantity = data.get("quantity")
#         gst = data.get("gst")
#         taxable_amount = data.get("taxable_amount")
#         total_amount = data.get("total_amount")
#         conn.execute("INSERT INTO item (invoice_id, item, hsn_code, price, quantity, gst, taxable_amount, total_amount) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
#                      (invoice_id, item, hsn_code, price, quantity, gst, taxable_amount, total_amount))
#         conn.commit()
#         conn.close()
#         return {'status': 'success'}
#     except Exception as e:
#         return {'status': 'error', 'message': str(e)}

# # Get all items route
# @app.route("/item_list", methods=["GET"])
# def get_items():
#     try:
#         conn = get_db_connection()
#         cursor = conn.execute("SELECT id, invoice_id, item, hsn_code, price, quantity, gst, taxable_amount, total_amount FROM item")
#         items = cursor.fetchall()
#         conn.close()
#         return {'status': 'success', 'items': [dict(item) for item in items]}
#     except Exception as e:
#         return {'status': 'error', 'message': str(e)}
    

# if __name__ == "__main__":
#     app.run()
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///npay.db'
db = SQLAlchemy(app)

# Registration model
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization_name = db.Column(db.String(100), nullable=False)
    roc = db.Column(db.String(50), nullable=False)
    date_of_incorporation = db.Column(db.Date, nullable=False)
    organization_pan = db.Column(db.String(20), nullable=False)
    upload_pan = db.Column(db.String(100), nullable=False)
    organization_tan = db.Column(db.String(20), nullable=False)
    organization_gst = db.Column(db.String(20), nullable=False)
    upload_gst = db.Column(db.String(100), nullable=False)
    organization_cin = db.Column(db.String(50), nullable=False)
    upload_cin = db.Column(db.String(100), nullable=False)
    official_email = db.Column(db.String(100), nullable=False)
    official_contact = db.Column(db.String(20), nullable=False)

# OTP model
class OTP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    otp = db.Column(db.Integer, nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)

# Invoice model
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gst = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_address = db.Column(db.String(200), nullable=False)
    invoice_number = db.Column(db.String(50), nullable=False)
    invoice_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    discount = db.Column(db.Float, nullable=False)
    terms = db.Column(db.String(200), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    items = db.relationship('Item', backref='invoice', lazy=True)

# Item model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
    item = db.Column(db.String(100), nullable=False)
    hsn_code = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    gst = db.Column(db.Float, nullable=False)
    taxable_amount = db.Column(db.Float, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)

# Create the database if it doesn't exist
with app.app_context():
    db.create_all()

# Registration route
@app.route("/registration", methods=["POST"])
def registration():
    try:
        data = request.json
        registration = Registration(
            organization_name=data.get("organization_name"),
            roc=data.get("roc"),
            date_of_incorporation=datetime.strptime(data.get("date_of_incorporation"), "%Y-%m-%d").date(),
            organization_pan=data.get("organization_pan"),
            upload_pan=data.get("upload_pan"),
            organization_tan=data.get("organization_tan"),
            organization_gst=data.get("organization_gst"),
            upload_gst=data.get("upload_gst"),
            organization_cin=data.get("organization_cin"),
            upload_cin=data.get("upload_cin"),
            official_email=data.get("official_email"),
            official_contact=data.get("official_contact")
        )
        db.session.add(registration)
        db.session.commit()
        return {'status': 'success'}
    except Exception as e:
        db.session.rollback()
        return {'status': 'error', 'message': str(e)}

# OTP Sending route   
@app.route("/send_otp", methods=["POST"])
def send_otp():
    email = request.json.get("email")
    otp = random.randint(100000, 999999)
    # Insert the otp into the database
    otp_entry = OTP(otp=otp, mobile_number=email)
    db.session.add(otp_entry)
    db.session.commit()
    # Send OTP to the user
    return {'status': 'OTP Sent successfully', 'otp': str(otp)}

# OTP Verification route
@app.route("/verify_otp", methods=["POST"])
def verify_otp():
    audit_id = request.json.get("audit_id")
    otp_entry = OTP.query.filter_by(id=audit_id, is_verified=False).first()
    if otp_entry:
        otp_entry.is_verified = True
        db.session.commit()
        return {'status': 'OTP Verified successfully'}
    return {'status': 'OTP Verification failed'}

# Invoice route
@app.route("/invoice", methods=["POST"])
def invoice():
    try:
        data = request.json
        name = data.get("name")
        gst = data.get("gst")
        address = data.get("address")
        customer_name = data.get("customer_name")
        customer_address = data.get("customer_address")
        invoice_number = data.get("invoice_number")
        invoice_date = datetime.strptime(data.get("invoice_date"), "%Y-%m-%d").date()
        due_date = datetime.strptime(data.get("due_date"), "%Y-%m-%d").date()
        discount = data.get("discount")
        terms = data.get("terms")
        total_amount = data.get("total_amount")

        invoice = Invoice(name=name, gst=gst, address=address, customer_name=customer_name,
                           customer_address=customer_address, invoice_number=invoice_number,
                           invoice_date=invoice_date, due_date=due_date, discount=discount,
                           terms=terms, total_amount=total_amount)

        db.session.add(invoice)
        db.session.commit()

        return {'status': 'success'}
    except Exception as e:
        db.session.rollback()
        return {'status': 'error', 'message': str(e)}

# Item route
@app.route("/item", methods=["POST"])
def item():
    try:
        data = request.json
        invoice_id = data.get("invoice_id")
        item = data.get("item")
        hsn_code = data.get("hsn_code")
        price = data.get("price")
        quantity = data.get("quantity")
        gst = data.get("gst")
        taxable_amount = data.get("taxable_amount")
        total_amount = data.get("total_amount")

        item = Item(invoice_id=invoice_id, item=item, hsn_code=hsn_code, price=price,
                    quantity=quantity, gst=gst, taxable_amount=taxable_amount, total_amount=total_amount)

        db.session.add(item)
        db.session.commit()

        return {'status': 'success'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}



if __name__ == "__main__":
    app.run()