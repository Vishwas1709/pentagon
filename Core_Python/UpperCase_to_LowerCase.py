print("Enter the string: ")
str = input()
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
        newstr = newstr + data
    i = i + 1
print("The converted string is: ", newstr)

#Inbild function for Upper case to lower case
# str = "Hello World"
# print(str.lower())