'''def Swap_String(s1):
    nstr=""
    for i in range (len(s1)):
        if "a" <=s1[i] <="z":
            nstr=nstr+chr(ord(s1[i])-32)
        elif "A" <=s1[i] <= "Z" :
            nstr=nstr+chr(ord(s1[i])+32)
        else:
            nstr=nstr+s1[i]
    return nstr

s1=input("Enter the string")
print(f"Original String is {s1}")
res=Swap_String(s1)
print(f"The swaped string is {res}")'''


#write a program to sum up each individual digit in a given string

def sum_character_digit(s1):
    sum=0
    for i in range(len(s1)):
        if "0" <= s1[i] <= "9":
            sum=sum+(ord(s1[i])-48)
    return sum


s1=input("Enter the string")
res=sum_character_digit(s1)
print(res)
