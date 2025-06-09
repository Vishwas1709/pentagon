class Radio:
    def turn_on(self,x):
        if x == 1:
            print("Radio is now ON")
        else:
            print("Radio is OFF")
class Car:
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.r=Radio()
c=Car(60,120)
print(c.min)
print(c.max)
c.r.turn_on(1)  # Turning on the radio
c.r.turn_on(0)  # Turning off the radio
# In this example, we have a `Radio` class that can be turned on or off, and a `Car` class that contains an instance of the `Radio` class.


