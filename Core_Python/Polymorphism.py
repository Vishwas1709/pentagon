class Plane:
    def take_off(self):
        print("Plane is taking off")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landing")
class Cargo(Plane):
    def take_off(self):
        print("Cargo plane is taking off")
    def fly(self):
        print("Cargo plane is flying")
    def land(self):
        print("Cargo plane is landing")
class Passenger(Plane):
    def take_off(self):
        print("Passenger plane is taking off")
    def fly(self):
        print("Passenger plane is flying")
    def land(self):
        print("Passenger plane is landing")
class Fighter(Plane):
    def take_off(self):
        print("Fighter plane is taking off")
    def fly(self):
        print("Fighter plane is flying")
    def land(self):
        print("Fighter plane is landing")
c=Cargo()
p=Passenger()
f=Fighter()

def allowplane(ref):
    ref.take_off()
    ref.fly()
    ref.land()
allowplane(c)
allowplane(p)
allowplane(f)
# In this example, we have a base class `Plane` and three derived classes: `Cargo`, `Passenger`, and `Fighter`.