def fun1():
    print("Inside fun1")
def fun2(a,b):
    c=a+b
    print("Sum is ",c)
def display(ptr1,ptr2):
    ptr1()
    x=50
    y=60
    ptr2(x,y)
fun1()
x=40
y=50
fun2(x,y)
ref1=fun1
ref2=fun2
display(ref1,ref2)
    