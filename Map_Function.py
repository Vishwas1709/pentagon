def operation(data):
    return data+10
l=[]
i=0
while(i<=4):
    print("Enter a number: ")
    num=int(input())
    l.insert(i, num)
    i=i+1
print(l)
l2=map(operation, l)
print(l2)       #Map addresses the function and returns the object
l1=list(map(operation, l))
print(l1)
print("End of program")


#Using Lambda function

k=list(map(lambda data: (data+10), l))
print(k) 