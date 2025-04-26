# str="     Rama Is Dancing       "
# print(str)
# str1= str.lstrip()
# print(str1)
# str2= str.rstrip()
# print(str2)
# str3= str.strip()
# print(str3)


# print("Enter a string: ")
# str=input()
# i=0
# newstr=""
# while (i<=len(str)-1):
#     data=str[i]
#     if (data == " "):
#         i+=1
#     else:
#         newstr+=data
#         i+=1
# print("String after removing spaces: ",newstr)
# # str="     Rama Is Dancing       "
        

#Another way to remove spaces from a string 

print("Enter a string: ")
str=input()
# str1=str.replace(" ","")
str1="".join(str.split())
print("String after removing spaces: ",str1)