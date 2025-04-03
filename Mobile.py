class Mobile:
    def __init__ (self):
        self.brand="Nokia"      #1st type of variable declara
        self.cost=1999
    def work(self):
        self.charge=90          #2nd type
        print(self.charge)
m1=Mobile()
print(m1.brand)
m1.work()
m1.color="Black"   #3rd type
print(m1.color)
