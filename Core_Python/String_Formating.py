print("Enter a string: ")
str=input()
print("Hi {}".format(str))
print("Name ={}".format(str))

str="Ravana"
print(str)
print(str[0])
print(str[4])
print(str[5])
# str[4]="m" # Error: TypeError: 'str' object does not support item assignment
str1=str.replace("R","M")
print(str1)