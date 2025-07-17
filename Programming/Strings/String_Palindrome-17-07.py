def filteration(s1):
    nstr=""
    for i in range(len(s1)):
        if "A" <= s1[i] <="Z":
            nstr=nstr+chr(ord(s1[i])+32)
        elif ("a" <= s1[i] <='z') or ('0'<=s1[i]<="9"):
            nstr=nstr+s1[i]
    return nstr


def string_palindrome(s1):
    s1=filteration(s1)
    print(s1)
    i=0
    j=len(s1)-1
    while i<j:
        if s1[i]!=s1[j]:
            return False
        i+=1
        j-=1
    return True

s1=input("Enter the string")
res=string_palindrome(s1)
if res: 
    print("The string is palindrome")
else:
    print("The given string is not a palindrome")
