# #1
# n=int(input("Enter the number"))
# noc=1
# for i in range(1,(n*2)):
#     for j in range(n,noc-1,-1):
#         print(f"{noc}",end="")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1

# #2
# n=int(input("Enter the number"))
# noc=1
# for i in range(1,(n*2)):
#     for j in range(n,noc-1,-1):
#         print(f"{j}",end="")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1
    
#Assignment Question
#4321
#321
#21
#1
#21
#321
#4321

n=int(input("Enter the number"))
noc=n
for i in range(1,(n*2)):
    for j in range(noc,1-1,-1):
        print(f"{j}",end="")
    print()
    if i<n:
        noc-=1
    else:
        noc+=1
    

     

