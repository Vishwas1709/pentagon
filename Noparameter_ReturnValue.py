class Calculator():
    def __init__(self):
        self.a=10
        self.b=20
    def display(self):
        x=100
        y=200
        z=x+y
        return z
c1=Calculator()
print(c1.a)
print(c1.b)
ref= c1.display()
print(ref)
