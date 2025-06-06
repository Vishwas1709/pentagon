# def dn(n):
#     if n<=0:
#         return 
#     print(n)
#     dn(n-1)
    
# n=int(input("Enter a number: "))
# dn(n)

# increment 
def dn(n):
    if n<=0:
        return 
    print(n)
    dn(n-1)
    print(n)
n=int(input("Enter a number: "))
dn(n)



