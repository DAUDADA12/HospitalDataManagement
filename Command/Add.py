# Command/AddPatient.py

import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="Kolkata@12",
        database="patient"
    )

def add_Patient(name=None, reason=None ,bill=None, date=None, doctor=None):
    if name is None or bill is None or date is None or reason is None or doctor is None:
        return "Usage: To add Patient, specify 'name', 'bill', and 'quantity'."
    db = connect_db()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO Patients (name, bill, date, reason, doctor) VALUES (%s, %s, %s, %s, %s)", (name, bill, date, reason, doctor))
        db.commit()
        return "Patient added successfully."
    except Exception as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        db.close()

def ByDefault():
    name = input("Enter Patient name: ")
    reason = input("Enter the reason: ")
    bill = float(input("Enter Bill: "))
    date = str(input("Enter Date[DD/MM/YYYY]: "))
    doctorname = input("Enter Doctor name: ")
    return add_Patient(name, reason, bill, date, doctorname)

