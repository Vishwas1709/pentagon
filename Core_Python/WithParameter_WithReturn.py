class Calculator:
    def __init__(self):
        self.a=10
        self.b=20
    def display(self,x,y):
        z=x+y
        return z
c1=Calculator()
print(c1.a)
print(c1.b)
x=100
y=200
ref=c1.display(x,y)
print(ref)