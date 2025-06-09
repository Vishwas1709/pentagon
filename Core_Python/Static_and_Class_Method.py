class Demo:
    x=10 # class variable # static variable
    def __init__(self):
        self.y=20
        self.z=30
    def disp(self):
        print(self.y)
        print(self.z)   
    @staticmethod
    def static_disp():
        print("This is a static method")
        print(Demo.x)
        Demo.x=20 # class variable
        print(Demo.x)
    @classmethod
    def class_disp(cls):
        print("This is a class method")
        print(cls.x)
        cls.x=30 # class variable
        print(cls.x)
d=Demo()
d.disp()
d.static_disp()
d.class_disp()

    

    
    