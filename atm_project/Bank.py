class Account:
    def __init__ (self, name,acc_no, balance):
        self.name=name
        self.Acc_no=acc_no
        self.balance=balance
        self.pin=None
        self.transaction=[]

    def deposit(self, amount):
        if amount % 100 ==0:
            self.balance += amount

    def withdrawal (self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def setPin (self):
        self.pin = int(input("Set Your Pin "))

    def verifyPin(self):
        entered_pin= int(input("Enter Your Pin "))
        if entered_pin == self.pin:
            return True
        return False
    def changePin(self):
        changed_pin =int (input("Enter differnt pin"))
        if self.pin != changed_pin:
            self.pin= changed_pin
        else:
            print("Enter the differnt pin ")


        
