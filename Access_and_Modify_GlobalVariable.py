a=999
def fun1():
    global a
    a=888
    b=777
    print(a)
    print(b)
def fun2():
    global a
    a=666
    c=555
    print(a)
    print(c)
print(a)
fun1()
fun2()
print(a)