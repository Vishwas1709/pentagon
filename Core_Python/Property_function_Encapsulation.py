class Student:
    def __init__(self):
        self.__name1=" "
        self.__name2=" "
    def getdata1(self):
        return self.__name1
    def setdata1(self,value):
        self.__name1=value
    getset=property(getdata1,setdata1)
    def NAME2(self):
        return self.__name2
    def NAME1(self,value):
        self.__name2=value
    getset2=property(NAME2,NAME1)
s=Student()
s.getset="John"
res1=s.getset
print(res1) # John
s.getset2="Doe"
res2=s.getset2
print(res2) # Doe
