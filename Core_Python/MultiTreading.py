import time
from threading import Thread
class Task1(Thread):
    def run(self):
        name = ["Rama", "Sita", "Lakshman", "Hanuman"]
        for i in name:
            print(i)
            time.sleep(2)
class Task2(Thread):
    def run(self):
        for i in range(10):
            print(i)
            time.sleep(2)
class Task3(Thread):
    def run(self):
        a = 10
        b = 20
        c = a + b
        print("Sum is:", c)
        time.sleep(2)
t1=Task1()
t2=Task2()
t3=Task3()
t1.start()  # Start Task1 thread
t2.start()  # Start Task2 thread
t3.start()  # Start Task3 thread
