import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kolkata@12",
        database="patient"
    )

def edit_Patient(name, new_bill=None, new_date=None, new_doctor=None):
    db = connect_db()
    cursor = db.cursor()
    try:
        if new_bill:
            cursor.execute("UPDATE Patients SET bill = %s WHERE name = %s", (new_bill, name))
        if new_date:
            cursor.execute("UPDATE Patients SET date = %s WHERE name = %s", (new_date, name))
        if new_doctor:
            cursor.execute("UPDATE Patients SET doctor = %s WHERE name = %s", (new_doctor, name))
        db.commit()
        print("Patient updated successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        db.close()

def ByDefault():
    name = input("Enter Patient name to edit: ")
    new_bill = input("Enter new bill (leave blank if no change): ")
    new_date = input("Enter new Date (leave blank if no change): ")
    new_doctor = input("Enter new Doctor Name (leave blank if no change): ")
    
    new_bill = float(new_bill) if new_bill else None
    new_date = int(new_date) if new_date else None
    
    edit_Patient(name, new_bill, new_date, new_doctor)
