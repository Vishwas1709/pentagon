# write a program to fibonacci series
'''
def fibo(n,n1,n2):
    if n<=0:
        return
    print(n1,end=" ")
    fibo((n-1),n2,(n1+n2))
n=int(input("Enter the number"))
fibo(n,0,1)
'''

#Write a program to print n fibonacci number

def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
n=int(input("Enter the number"))
res=fibo(n)
print(res)