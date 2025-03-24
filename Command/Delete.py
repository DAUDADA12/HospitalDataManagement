import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kolkata@12",
        database="patient"
    )

def delete_Patient(name):
    db = connect_db()
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM Patients WHERE name = %s", (name,))
        db.commit()
        print("Patient deleted successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        db.close()

def ByDefault():
    name = input("Enter Patient name: ")
    delete_Patient(name)

