'''/"Student code: ":" ",
    "Name: ":" ",
    "course: ":" ",
    "joined: ":" ",
    "Duration: ":" ",
    "Phone: ":" ",
    "city: ":" "  /'''
class stud():
    # Starting
    def __init__(self):
        self.student_1_={
            "Student  code: ":"00001",
            "Name":"Kousik kumar",
            "course":"ADPAD",
            "joined":"08-01-2024",
            "Duration":"80 days",
            "Phone":"9442191979",
            "city":"karaikudi"
        }
        self.student_2_={
            "Student  code: ":"00002",
            "Name: ":"Abirami",
            "course: ":"JAVA",
            "joined: ":"XX-XX-XXXX",
            "Duration: ":"120 days",
            "Phone: ":"XXXXXXXXXX",
            "city: ":"karaikudi"
        }
    def fee(self):
        self.student_f1_=10000
        self.student_f2_=10000  
    def display(self):
        if(code==1):
            for a in self.student_1_.items():
                print(a) 
            print("\nStudent fee: ",self.student_f1_)       
        elif(code==2):
            for a in self.student_2_.items():
                print(a) 
            print("\nStudent fee: ",self.student_f2_) #Ending
code=int(input("Enter the student code: "))
v=stud()
v.fee()
v.display()