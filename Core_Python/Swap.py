str=input("Enter the string: ")
i=0
newstr = ""
while (i<=len(str)-1):
    data=str[i]
    ascii = ord(data)
    if(ascii >= 65 and ascii <= 90):
        newascii = ascii +32
        convchar = chr(newascii)
        newstr = newstr + convchar
    else:
        newascii = ascii - 32
        convchar = chr(newascii)
        newstr = newstr + convchar
    
    i = i + 1
print("The converted string is: ", newstr)


# Inbuild function for swapping case
# str = "Hello World"
# print(str.swapcase())
# Inbuild function for swapping case