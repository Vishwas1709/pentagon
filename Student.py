class Student:
    def __init__ (self):
        self.name="Vishwas"
        self.usn=123
        self.age=21
    def eat(self):
        print("Vishwas Is eating")
    def study(self):
        print("Vishwas Is not studing")
s1=Student()
print(s1.name)
print(s1.usn)
print(s1.age)
s1.study()