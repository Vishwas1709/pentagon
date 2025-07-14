def Lower_case(s1):
    nstr=""
    for i in range(len(s1)):
        if "A" <= s1[i] <="Z":
            nstr=nstr+ chr(ord(s1[i])+32)
        else:
            nstr=nstr+s1[i]
    return nstr




s1=input("Enter the string")
print(f"Original string is {s1}")
res=Lower_case(s1)
print(f"the Lower case letters are {res}")