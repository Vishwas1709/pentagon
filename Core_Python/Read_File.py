'''
print("Enter the file name")
fname=input()
fptr=open(fname,"r")
# data1=fptr.read()
# print(data1)

# data2=fptr.read(10) # Read the first 10 characters from the file
# print(data2)

# data3=fptr.readline() # Read the first line from the file
# print(data3)

data4=fptr.readlines() # Read all lines from the file into a list
print(data4)
'''

str1="Rama is eating"
print(len(str1)) # Length of the string
str2=str1.split() # Split the string into a list of words
print(str2) # ['Rama', 'is', 'eating']
print(len(str2)) # Length of the list

fptr=open("emp.txt","r")
print(fptr.name) # Name of the file
print(fptr.mode) # Mode in which the file is opened
print(fptr.writable()) # Check if the file is writable
print(fptr.readable()) # Check if the file is readable
print(fptr.closed) # Check if the file is closed
fptr.close() # Close the file
print(fptr.closed) # Check if the file is closed again
