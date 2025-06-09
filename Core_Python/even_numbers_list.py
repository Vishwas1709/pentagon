def even(num):
    if (num % 2 == 0):
        return True
    else:
        return False
L=[]
i=0
while(i<=4):
    data=int(input("Enter a number: "))
    if even(data):
        L.insert(i, data)
        i=i+1
print(L)
i=0
while(i<=4):
    num1=L[i]
    status=even(num1)
    if status:
        print(L[i])
    i=i+1
print("End of program")


#Using Filter function
def even(num):
    if (num % 2 == 0):
        return True
    else:
        return False
L=[]
i=0
while(i<=4):
    data=int(input("Enter a number: "))
    L.insert(i, data)
    i=i+1
print(L)
L2=(filter(even, L))
print(L2)       #Filter addresses the function and returns the object
L1=list(filter(even, L))
print(L1)
print("End of program")

#Using Lambda function

L=[]
i=0
while(i<=4):
    data=int(input("Enter a number: "))
    L.insert(i, data)
    i=i+1
print(L)
L2=(filter(lambda num: (num % 2 == 0), L))
print(L2)       #Filter addresses the function and returns the object
L1=list(filter(lambda num: (num % 2 == 0), L))
print(L1)
print("End of program")