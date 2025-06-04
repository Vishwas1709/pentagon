#WAP to print all the prime number's of a defined range.
# def is_prime(n):
#     if n <= 1:
#         return False
#     # check from 2 to sqrt(n)
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# start = int(input("Enter start of range: "))
# end = int(input("Enter end of range: "))

# print("Prime numbers between", start, "and", end, "are:")

# for num in range(start, end + 1):
#     if is_prime(num):
#         print(num, end=" ")
'''
def isprime(n):
    count=0

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
    return count==2

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

if start>end:
    print("Invalid Range")
else:
    print("Prime numbers between", start, "and", end, "are:")

    for num in range(start, end + 1):
        flag=isprime(num)
        if flag:
            print(num, end=" ")
'''

#WAP to print all the prime and non-prime number's of a defined range seperateley.

# def is_prime(n):
#     if n <= 1:
#         return False
#     # check from 2 to sqrt(n)
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# start = int(input("Enter start of range: "))
# end = int(input("Enter end of range: "))

# prime_numbers = []
# nonprime_numbers = []

# for num in range(start, end + 1):
#     if is_prime(num):
#         if True:
#             prime_numbers.append(num)
#     else:
#            nonprime_numbers.append(num)

# print("Prime numbers between", start, "and", end, "are:", prime_numbers)
# print("Non-prime numbers between", start, "and", end, "are:", nonprime_numbers)
'''
def isprime(n):
    count=0

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
    return count==2

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
if start>end:
    print("Invalid Range")
else:

    print("Prime numbers between", start, "and", end, "are:")

    for num in range(start, end + 1):
        flag=isprime(num)
        if flag:
            print(num, end=" ")
    
    for num in range(start, end + 1):
        flag=isprime(num)
        if not flag:
            print(num, end=" ")

#WAP to print first "n" prime numbers.
'''

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# num= int(input("Enter how many prime numbers to print: "))

# count = 0  
# n = 2   

# print(f"First {n} prime numbers are:")

# while count < num:
#     if is_prime(n):
#         print(n, end=" ")
#         count += 1
#     n += 1

'''
def isprime(n):
    count=0

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
    return count==2

n = int(input("Enter start of number: "))
num=1
count=0
while count<n:
    if isprime(num):
        print(num,end=" ")
        count+=1
    num+=1

#WAP to print all the arm strong numbers of a defined range
'''
'''
def countdigit(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

def isarmstrong(pow, b):
    asn = 0
    temp = b
    while temp > 0:
        base = temp % 10
        asn += base ** pow
        temp //= 10
    return asn

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

if start>end:
    print("Invalid Range")
else:
    print(f"\nArmstrong numbers between {start} and {end} are:")

    for num in range(start, end + 1):
        digits = countdigit(num)
        armstrong_val = isarmstrong(digits, num)
        if armstrong_val == num:
            print(num, end=" ")
'''

#WAP to print all the asn and non-asn number's of a defined range seperateley.
'''
def countdigit(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

def is_armstrong(num):
    power = countdigit(num)
    temp = num
    result = 0
    while temp > 0:
        digit = temp % 10
        result += digit ** power
        temp //= 10
    return result == num


start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

asn_numbers = []
non_asn_numbers = []


for num in range(start, end + 1):
    if is_armstrong(num):
        asn_numbers.append(num)
    else:
        non_asn_numbers.append(num)

print(f"\nArmstrong numbers between {start} and {end}:")
print(asn_numbers)

print(f"\nNon-Armstrong numbers between {start} and {end}:")
print(non_asn_numbers)

'''
# WAP to print first "n" armstrong numbers.

'''
def countdigit(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

def is_armstrong(num):
    power = countdigit(num)
    temp = num
    result = 0
    while temp > 0:
        digit = temp % 10
        result += digit ** power
        temp //= 10
    return result == num


n = int(input("Enter how many Armstrong (asn) numbers to print: "))


count = 0
num = 1

print(f"\nFirst {n} Armstrong numbers are:")
while count < n:
    if is_armstrong(num):
        print(num, end=" ")
        count += 1
    num += 1
'''


            