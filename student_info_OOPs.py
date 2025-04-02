class Student:
    def __init__(self):
        self.stu_code = [
            "B2455R1017501", "B2455R1017502", "B2455R1017503", 
            "B2455R1017504", "B2455R1017506", "B2455R1017507", 
            "B2455R1017508", "B2455R10175010", "B2455R10175016", "B2455R10175018"
        ]
        self.aced_info = {
            "B2455R1017501": "Name: Shivam Dwivedi, Program: B.Tech., Course: CSE (Cyber Security), Academic Year: 1st Year",
            "B2455R1017502": "Name: Deependra Prajapati, Program: B.Tech., Course: CSE (Cyber Security), Academic Year: 1st Year",
            "B2455R1017504": "Name: Yogesh Mishra, Program: B.Tech., Course: CSE (Cyber Security), Academic Year: 1st Year",
            "B2455R1017505": "Name: Dheerendra Mishra, Program: B.Tech., Course: CSE (Cyber Security), Academic Year: 1st Year",
            "B2455R1017507": "Name: Nikita , Program: B.Tech., Course: CSE (Cyber Security), Academic Year: 1st Year",
            "B2455R1017508": "Name: Vikash Verma, Program: B.Tech., Course: CSE (Cyber Security), Academic Year: 1st Year",
            "B2455R1017503": "Name: Ayush Kumar, Program: B.Tech., Course: CSE (Cyber Security), Academic Year: 1st Year",
            "B2455R10175010": "Name: Moluram Kushwaha, Program: B.Tech., Course: CSE (Cyber Security), Academic Year: 1st Year",
            "B2455R10175016": "Name: Harsh Shukla, Program: B.Tech., Course: CSE (Cyber Security), Academic Year: 1st Year",
            "B2455R10175018": "Name: Aryan Soni, Program: B.Tech., Course: CSE (Cyber Security), Academic Year: 1st Year"
        }
        # pre defined password which is known to user
        self.saved_password = "AKS1545"

    def show_info(self):
        password = input("Enter password: ")
        
        if password == self.saved_password:
            print("\nAvailable Student Codes:")
            for code in self.stu_code:
                print(code)
            while True:
                stud_code = input("\nEnter student code from the list above or Stop to exit: ").upper()
                if stud_code == "STOP":
                    break
                elif stud_code in self.aced_info:
                    print(f"\nStudent Information:\n{self.aced_info[stud_code]}")
                else:
                    print("Invalid Student Code")
        else:
            print("Wrong Password")


student = Student()
student.show_info()