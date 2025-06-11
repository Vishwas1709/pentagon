# def factor(i,n):
#     if i*i>n:
#         return 
#     if n%i==0:
#         print(i,end=" ")
#         if i!=(n//i):
#             print(n//i, end=" ")
#     i=i+1
#     factor(i,n)
# n=int(input("Enter the number"))
# i=1
# factor(i,n)

# prime numbers in recussion  

# def isprime(i,n,count):
#     if i*i>n:
#         return count==2
#     if n%i==0:
#         count+=1
#         if i!=(n//i):
#             count+=1
#     i=i+1
#     return isprime(i,n,count)
# n=int(input("Enter the number"))
# i=1
# count=0
# res=isprime(i,n,count)
# if res:
#     print(f"{n} is a prime number ")
# else:
#     print(f"{n} is not a prime number")

#GCD

def findgcd(n1,n2,i,gcd):
    if i>n1:
        return gcd
    if n1%i==0 and n2%i==0:
        gcd=i
    return findgcd(n1,n2,(i+1),gcd)

n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))

if n1>n2:
    n1,n2=n2,n1
res=findgcd(n1,n2,1,1)
print(f" GCD of {n1},{n2} is {res}")