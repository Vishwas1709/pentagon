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
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    a, b = b, a
for i in range(1, b + 1):
    if (a * i) % b == 0:
        lcm = a * i
print("The LCM of", a, "and", b, "is:", lcm)