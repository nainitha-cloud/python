class student:
    def __init__(self,name,r_no):
        self.name=name
        self.r_no=r_no
        print("name is:",self.name)
        print("r_no is:",self.r_no)
    def marks(self,marks):
        self.marks=marks
        print("marks are:",self.marks)
s1=student("smiley",567)
s1.marks(89)

s2=student("janu",491)
s2.marks(79)

s3=student("chai",547)
s3.marks(49)

s4=student("ram",527)
s4.marks(59)

s5=student("sri",537)
s5.marks(79)
