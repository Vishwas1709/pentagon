class Demo:
    x=10  # class variable  # static variable
    def __init__(self):
        self.y=10
        self.z=20
    def disp(self):
        print(self.y)  # instance variable
        print(self.z)
        res=40+50
        print(res)
d=Demo()
d.disp()
print(Demo.x)  # class variable
