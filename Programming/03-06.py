'''
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
if count == 2:
    print("\nThe number is prime.")
else:
    print("\nThe number is not prime.")
print("\nTotal number of factors:", count)
print("\nTotal Cycles:", total)


# inbuild function

n=int(input("Enter the number "))
from sympy import isprime
prime=isprime(n) 
if prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

'''
# write a program to display the hcf or gcd of two numbers

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
# print("The HCF or GCD of", a, "and", b, "is:", hcf)

# write a program to display the lcm of two numbers

# def lcm_loop(x, y):
#     if x > y:
#         greater = x
#     else:
#         greater = y
#         while True:
#             if greater % x == 0 and greater % y == 0:
#                 return greater
#             greater += 1
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# lcm = lcm_loop(a, b)
# print("The LCM of", a, "and", b, "is:", lcm)

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
i=1
hcf=1
if a > b:
    a,b=b,a
while i <= a:
    if a % i == 0 and b % i == 0:
        hcf = i
        lcm = (a * b) // hcf
    i += 1
print("The HCF or GCD of", a, "and", b, "is:", hcf)
print("The LCM of", a, "and", b, "is:", lcm)