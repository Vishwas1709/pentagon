def fun1():
    print("Inside fun1")
def fun2(a,b):
    c=a+b
    print("sum is",c)
def display(ptr1,ptr2):
    ptr1()
    x=50
    y=60
    ptr2(x,y)
fun1()
fun2(10,20)
ptr3=fun1
ptr4=fun2
ptr3()
a=30
b=40
ptr4(a,b)
display(ptr3,ptr4)
