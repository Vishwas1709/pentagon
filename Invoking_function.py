def fun1():
    print("Invoking fun1")
def fun2(x,y):
    z=x+y 
    print(z)
fun1()
a=10
b=20
fun2(a,b)
ptr1=fun1
ptr2=fun2
print(ptr1)
print(fun1)
ptr1()
ptr2(40,50)
