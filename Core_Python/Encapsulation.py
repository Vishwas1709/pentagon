class Book:
    def __init__(self,value):
        self.__pages=value
    def setter(self,value):
        if value>0:
            self.__pages=value
    def getter(self):
        return self.__pages
b1=Book(100)
b1.setter(200)
res =b1.getter()
print(res) # 200
b1.setter(-50) # This will not change the value since -50 is not valid
res =b1.getter()
print(res) # 200
