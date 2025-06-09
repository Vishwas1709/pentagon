class Demo:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c= 10
        print(self)
    def add(self):
        x = 100
        y = 200
        print(self.a)
        print(self.b)
d1=Demo()
print(d1.a)
print(d1.b)
d1.add()
print(d1)
print(id(d1.a))
print(id(d1.c))

