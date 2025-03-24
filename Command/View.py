# Command/ViewPatient.py

import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="Kolkata@12",
        database="patient"
    )

def view_Patients():
    db = connect_db()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM Patients")
        results = cursor.fetchall()
        if not results:
            return "No Patients found."
        response = "ID | Name       | Reason             | Bill       | Date       | Doctor Attended |\n"
        response += "-" * 35 + "\n"
        for row in results:
            response += f"{row[0]:<3}| {row[1]:<10}| {row[2]:<18} |{row[3]:<10}| {row[4]:<10} | {row[5]:<15} |\n"
        return response
    except Exception as e:
        return f"Error: {e}"
    finally:
        cursor.close()
        db.close()

def ByDefault():
    return view_Patients()
