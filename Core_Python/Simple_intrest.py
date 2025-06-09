class Farmer:
    r= 2.5  # Static variable
    def __init__(self, p1, t1):
        self.p = p1
        self.t = t1
    def display(self):
        SI= (self.p * Farmer.r * self.t) / 100
        print("Simple Interest is: ", SI)
f1= Farmer(100000, 2)
f2= Farmer(200000, 3)
f1.display()
f2.display()
# print(f1.r)  # Accessing static variable using object
# print(Farmer.r)  # Accessing static variable using class name
# print(f1.p)  # Accessing instance variable using object
# print(f2.p)  # Accessing instance variable using object
