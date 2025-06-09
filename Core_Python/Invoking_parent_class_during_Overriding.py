class A:
    def display(self):
        print("Inside dispA")
class B(A):
    def display(self):
        print("Inside dispB")
class C(B):
    def display(self):
        print("Inside dispC")
class D(C):
    def display(self):
        print("Inside dispD")
        C.display(self)    # Invoking the parent class method explicitly
        B.display(self)    # Invoking the parent class method explicitly
        A.display(self)    # Invoking the grandparent class method explicitly
d = D()
d.display()  # This will call the display method of class D, which in turn calls the parent class methods explicitly
