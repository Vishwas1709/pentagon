import time
class Demo:
    def printName(self):
        name=["Rama","Sita","Lakshman","Hanuman"]
        for i in name:
            print(i)
            time.sleep(2)
    def printNumbers(self):
        for i in range(10):
            print(i)
            time.sleep(2)
    def add(slef):
        a=10
        b=20
        c=a+b
        print("Sum is:",c)
        time.sleep(2)
d=Demo()
d.printName()  # Print names with a delay
d.printNumbers()  # Print numbers with a delay
d.add()  # Perform addition with a delay
