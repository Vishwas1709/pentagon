#1.
'''
aaaa
bbbb
cccc
dddd
'''
# n=int(input("Enter the number: "))
# for i in range(1, (n + 1)):
#     for j in range(1,(n+1)):
#         print(chr(96+i), end="")
#     print()

#2.
'''
A
BC
DEF
GHIJ
'''
# n=int(input("Enter the number: "))
# count=1
# for i in range(1,(n+1)):
#     for j in range(1,(i+1)):
#         print(chr(64+count), end="")
#         count+=1
#     print()
    

#3.
'''
abcd
abc
ab
a
'''
# n=int(input("Enter the number: "))
# for i in range(n,1-1,-1):
#     for j in range(1, (i + 1)):
#         print(chr(96 + j), end="")
#     print()

#4.
'''
abcd
ABCD
abcd
ABCD
'''
# n=int(input("Enter the number: "))
# for i in range(1,(n+1)):
#     if i%2==0:
#         for j in range(1, (n + 1)):
#             print(chr(64 + j), end="")
#     else:
#         for j in range(1, (n + 1)):
#             print(chr(96 + j), end="")
#     print()

#5.
'''
DcBa
DcBa
DcBa
DcBa
'''

# n=int(input("Enter the number: "))
# for i in range(1,(n+1)):
#     for j in range(n,0,-1):
#         if j%2==0:
#             print(chr(64+j), end="")
#         else:
#             print(chr(96+j), end="")
#     print()  

#6.
'''
AbCd
EfGh
IjKl
MnOp
'''

# n=int(input("Enter the number: "))
# count=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j%2==0:
#             print(chr(96+count), end="")
#             count+=1
#         else:
#             print(chr(64+count), end="")
#             count+=1
#     print()

#7.
'''
DDDD
CCC
BB
A
BB
CCC
DDDD
'''

# n=int(input("Enter the number: "))
# noc=n
# for i in range(1,(n*2)):
#     for j in range(1,noc+1):
#         print(chr(64+noc), end="")
#     print()
#     if i<n:
#         noc-=1
#     else: 
#         noc+=1

#8.
'''
ABCD
ABC
AB
A
AB
ABC
ABCD
'''
# n=int(input("Enter the number: "))
# noc=n
# for i in range(1,(n*2)):
#     for j in range(1,noc+1):
#         print(chr(64+j), end="")
#     print()
#     if i<n:
#         noc-=1
#     else: 
#         noc+=1
        
#9.
'''
ABCD
BCD
CD
D
CD
BCD
ABCD
'''

# n=int(input("Enter the number: "))
# noc=1
# for i in range(1,(n*2)):
#     for j in range(noc,n+1):
#         print(chr(64+j), end="")
#     print()
#     if i<n:
#         noc+=1
#     else: 
#         noc-=1

        
