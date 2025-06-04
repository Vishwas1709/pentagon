# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# i=1
# hcf=1
# if a > b:
#     a,b=b,a
# while i <= a:
#     if a % i == 0 and b % i == 0:
#         hcf = i
#     i += 1
# if hcf == 1:
#     print("The numbers are co-prime.")
# else:
#     print("The numbers are not co-prime.")
# print("The HCF or GCD of", a, "and", b, "is:", hcf)

# def hcf(a,b):
#     if a > b:
#         a, b = b, a
#     hcf = 1
#     for i in range(1, a + 1):
#         if a % i == 0 and b % i == 0:
#             hcf = i
#     return hcf == 1
        
# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))

# hcf =hcf(a, b)
# if  hcf:
#     print("The numbers are co-prime.")
# else:
#     print("The numbers are not co-prime.")

# write a program to print the first n fibonacci numbers 
#Using a list to store Fibonacci numbers
# def fibonacci(n):
#     a[0]=0
#     a[1]=1
#     for i in range(2, n):
#         a[i] = a[i - 1] + a[i - 2]
#     print("The first", n, "Fibonacci numbers are:")
#     for i in range(n):
#         print(a[i], end=" ")
# n= int(input("Enter a number"))
# a = [0] * n 
# fibonacci(n)

# write a program to print the first n fibonacci numbers 
# decrementing the value using a while loop
# def fibo(n):
#     n1=0
#     n2=1

#     while n > 0:
#         print(n1, end=" ")
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3
#         n -= 1
        
# n = int(input("Enter a number: "))
# fibo(n)

#incrementing the value using a while loop

def fibo(n):
    n1 = 0
    n2 = 1
    i=1
    while i<=n:
        print(n1, end=" ")
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        i += 1
n = int(input("Enter a number: "))
fibo(n)


# decrementing the value using a for loop
# def fibo(n):
#     n1=0
#     n2=1

#     for i in range(n+1, 1, -1):
#         print(n1, end=" ")
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3
        
# n = int(input("Enter a number: "))
# fibo(n)

# incrementing the value using a for loop
# def fibo(n):
#     n1=0
#     n2=1

#     for i in range(1, n + 1):
#         print(n1, end=" ")
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3
        
# n = int(input("Enter a number: "))
# fibo(n)