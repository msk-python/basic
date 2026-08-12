class_12th = {}

class student:
    def __init__(self, Name, Class, F_Name, Contact, fee) -> None:
        self.Name = Name
        self.Class = Class
        self.F_Name = F_Name
        self.Contact = Contact
        self.fee = fee

    def all_Students(self):
        print("\n#---------------------------------- All Students List ---------------------------------------#\n")
        print('Roll No.', 'Name', 'Class', "Father's Name", 'Contact', 'Received fee')
        for roll_no, details in class_12th.items():
            print(roll_no, details.Name, details.Class, details.F_Name, details.Contact, details.fee)
        print("\n#---------------------------------- All Students List ---------------------------------------#\n")

    def admission(self):
        try:
            last_roll_no = list(class_12th.keys())[-1]
            new_roll_no = last_roll_no + 1
        except:
            new_roll_no = 1001

        class_12th[new_roll_no] = self
        print(f"\nAdmission successful! Roll No: {new_roll_no}")

    def update_fee(self, roll_no, new_fee):
        if roll_no in class_12th:
            class_12th[roll_no].fee = new_fee
            print(f"Fee updated successfully for Roll No: {roll_no}")
        else:
            print("Roll number not found.")


# Main program loop
while True:
    print('Use Shortcuts:')
    print('''
1. Admission
2. All Students' Information
3. Update Student Fee
    ''')

    user = input("You: ")

    if user == "1":
        name = input("Student Name: ")
        section = input("Class Name: ")
        f_name = input("Father Name: ")
        contact = input("Contact: ")
        fee = input("Fee: ")

        a = student(name, section, f_name, contact, fee)
        a.admission()

    elif user == "2":
        a = student("", "", "", "", "")
        a.all_Students()

    elif user == "3":
        roll_no = int(input("Enter Roll No: "))
        new_fee = input("Enter New Fee: ")
        a = student("", "", "", "", "")
        a.update_fee(roll_no, new_fee)

    else:
        print("Invalid option, please try again.")
