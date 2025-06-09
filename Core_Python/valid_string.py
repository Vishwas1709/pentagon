str=input("Enter a string: ")
if str.isalpha():
    print("String contains only aphabets")
elif(str.isdigit()):
    print("String contains only digits")
elif(str.isalnum()):
    print("String contains both digits and alphabets")
else:
    print("Enter valid string")
    