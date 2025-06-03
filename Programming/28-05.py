
import math
from math import sqrt
n=int(input("Enter the number "))
count=0
total=0
for i in range(1,n+1):
    total+=1
    if n%i==0:
        print(i,end=" ")
        count+=1
print("\nTotal number of factors:", count)
print("\nTotal Cycles:", total)

'''
# effeciency version to find factors
n=int(input("Enter the number "))
total=0
count=0
sqrt_n = int(sqrt(n))
for i in range(1, sqrt_n + 1):
    total+=1
    if i*i <=n:
        if n%i==0:
            print(i,end=" ")
            count+=1
            if i != n // i:
                print(n//i,end=" ")
                count+=1
print("\nTotal Cycles:", total)
print("\nTotal number of factors:", count)
'''
            

# using the whiele loop
n=int(input("Enter the number "))
count=0
total=0
i=1
while i * i <= n:
    total+=1
    if n % i == 0:
        print(i,end=" ")
        count += 1
        if i != n//i:
            print(n//i,end=" ")
            count += 1
    i += 1
print("\nTotal number of factors:", count)
print("\nTotal Cycles:", total)

