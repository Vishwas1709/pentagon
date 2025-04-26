def function1():
    a=50
    b=20
    c=a+b
    print(c)
def function2():
    a=50
    b=20
    c=a+b
    return c
def function3(a,b):
    c=a+b
    print(c)
def function4(a,b):
    c=a+b
    return c
function1() # 70
return_value=function2() # 70
print(return_value) # 70
n=50
m=20
function3(n,m) # 70
return_value2=function4(n,m) # 70
print(return_value2) # 70
# The above code defines four functions: function1, function2, function3, and function4.
# function1 and function2 perform addition of two numbers, while function3 and function4 take parameters for the numbers to be added.


