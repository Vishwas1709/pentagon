#write a program to convert lower case letter to given string to UpperCase

def Upper_case(s1):
    nstr=""
    for i in range(len(s1)):
        if "a" <=s1[i] <="z":
            nstr=nstr+chr(ord(s1[i])-32)
        else:
            nstr=nstr+s1[i]
    return nstr



s1=input("Enter the string")
print("Original String ",s1)
res=Upper_case(s1)
print(f"The conerted Upper case is {res}")



