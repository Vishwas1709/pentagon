# # Patterns

# print("*")
# print()
# print("===================================================")

# # print Multiple stars in differnt lines
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     print("*")

# print("====================================")

# # print Multiple stars in same lines
# n=int(input("Enter the number"))
# for j in range(1,n+1):
#     print("*",end=" ")
# print("\n====================================")



# print("====================================")

# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     for  j in range (1,i+1):
#         print("*",end=" ")
#     print()

n=int(input("Enter the number"))
for i in range(1,n+1):
    for  j in range (1,i+1):
        print("*",end="")
    print()
