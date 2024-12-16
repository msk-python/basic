class_12th = {}

class student:
    def __init__(self, Name, Class, F_Name, Contact, fee) -> None:
        self.Name = Name
        self.Class = Class
        self.F_Name = F_Name
        self.Contact = Contact
        self.fee = fee

    def all_Students_List(self):
        print("\n#---------------------------------- All Students List ---------------------------------------#\n")
        
        print('Roll No.', 'Name', 'Class', "Father's Name", 'Contact', 'Received fee')
        for roll_no, details in class_12th.items():
            print(roll_no, details['Name'], details['Class'], details['F_Name'], details['Contact'], details['fee'])
            
        print("\n#---------------------------------- All Students List ---------------------------------------#\n")

    def admission(self):
        try:
            last_roll_no = list(class_12th.keys())[-1]
            new_roll_no = last_roll_no + 1
        except: new_roll_no = 1001

        class_12th[new_roll_no] = dict(
            Name=self.Name, Class=self.Class, F_Name=self.F_Name, Contact=self.Contact, fee=self.fee)
        print(f"\nAdmission successful! Roll No: {new_roll_no}")


# Main program loop
while True:
    print('Use Shortcuts:')
    print('''
1. Admission
2. All Students' Information
3. Update Student Fee
    ''')

    user = input("You: ")

    if "1" in user:
        name = input("Student Name: ")
        section = input("Class Name: ")
        f_name = input("Father Name: ")
        contact = input("Contact: ")
        fee = input("Fee: ")

        a = student(name, section, f_name, contact, fee)
        a.admission()

    elif "2" in user:
        a = student("", "", "", "", "")
        a.all_Students_List()

    else:
        print("Invalid option, please try again.")
