class OS:
    def __init__(self):
        self.status="True"
        print("OS is ready")
    def getOs(self):
        print("OS is still running")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.o=OS()
        print("Mobile is ready")
        print("With OS installed")
m=Mobile("Nokia")
print(m.mname)
print(m.o.status)
m.o.getOs()

