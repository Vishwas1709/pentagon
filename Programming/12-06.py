# GCD using Euclid's algorithm

# def gcd(n1, n2):
#     if n1<=0:
#         return n2
#     if n1<n2:
#         n1, n2 = n2, n1
#     return gcd((n1-n2),n2)
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# res = gcd(n1, n2)
# print(f"GCD of {n1}, {n2} is {res}")

# GCD using Euclid's algorithm (alternative)

# def gcd(n1, n2):
#     if n1<=0:
#         return n2
#     if n1<n2:
#         n1, n2 = n2, n1
#     return gcd((n1%n2),n2)  #   Using modulo operation  it is more efficient 
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# res = gcd(n1, n2)
# print(f"GCD of {n1}, {n2} is {res}")


# Factorial using recursion

# def fact(n):
#     if n<=1:
#         return n
#     return n * fact(n-1)
# n=int(input("Enter the number"))
# res=fact(n)
# print(f"Factorial of {n} is {res}")

# n naturals sum using recursion
def sum(n):
    if n<=1:
        return n
    return n + sum(n-1)
n = int(input("Enter the number: "))
res = sum(n)
print(f"Sum of first {n} natural numbers is {res}")
# Sum of digits using recursion

