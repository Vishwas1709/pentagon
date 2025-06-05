
def display4(n):
    print(n) #4
    display3(n-1)
def display3(n):
    print(n) #3
    display2(n-1)
def display2(n):
    print(n) #2
    display1(n-1)
def display1(n):
    print(n) #1
    

n=4
display4(n)