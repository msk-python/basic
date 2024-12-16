import sqlite3

def create_database():
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    
    # Create students table
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        class TEXT,
        fees_paid REAL DEFAULT 0
    )''')
    
    conn.commit()
    conn.close()

def add_student(name, age, student_class):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO students (name, age, class)
                      VALUES (?, ?, ?)''', (name, age, student_class))
    
    conn.commit()
    conn.close()
    print(f'Student {name} admitted successfully.')

def pay_fee(student_id, amount):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    
    # Fetch current fees paid
    cursor.execute('''SELECT fees_paid FROM students WHERE id = ?''', (student_id,))
    current_fees = cursor.fetchone()
    
    if current_fees:
        new_fees = current_fees[0] + amount
        cursor.execute('''UPDATE students SET fees_paid = ? WHERE id = ?''', (new_fees, student_id))
        conn.commit()
        print(f'Fees updated. Total fees paid: {new_fees}')
    else:
        print('Student not found.')
    
    conn.close()

def display_students():
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    
    cursor.execute('''SELECT * FROM students''')
    students = cursor.fetchall()
    
    print("ID\tName\tAge\tClass\tFees Paid")
    for student in students:
        print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}")
    
    conn.close()

def main():
    create_database()
    
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Pay Fees")
        print("3. Display Students")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            student_class = input("Enter student class: ")
            add_student(name, age, student_class)
        elif choice == '2':
            student_id = int(input("Enter student ID: "))
            amount = float(input("Enter amount to pay: "))
            pay_fee(student_id, amount)
        elif choice == '3':
            display_students()
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()