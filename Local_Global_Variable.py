a=999
def fun1():
    b=10
    print(b) # 10
    print(a) # 999
def fun2():
    a=1000
    b=20
    print(b) # 20
    print(a) # 1000
print(a) # 999
fun1() # 10 999
fun2() # 20 1000