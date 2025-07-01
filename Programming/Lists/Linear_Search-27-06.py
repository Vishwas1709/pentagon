# list=[1,3,4,6,4,5,7,8,9,10]
# n=int(input("Enter the number to search: "))
# for i in range(len(list)):
#     if list[i]==n:
#         print("Element found at index", i)
#         break
# else:
#     print("Element not found in the list")


# Write a program to search an element in a list using linear search
# without using function
'''
def createintlist():
    l = []
    while True:
        try:
            n = int(input("Enter the number "))
            l.append(n)
        except ValueError:
            return l
nums= createintlist()
target = int(input("Enter the number to search: "))
flag,index= False, -1
for i in range(len(nums)):
    if target==nums[i]:
        flag = True
        index = i
        break
if flag:
    print(f"{target} Element found at index", index)
else:
    print(f"{target} Element not found in the list")
    '''

#using function
'''
def createintlist():
    l = []
    while True:
        try:
            n = int(input("Enter the number "))
            l.append(n)
        except ValueError:
            return l
nums= createintlist()
target = int(input("Enter the number to search: "))
def linersearch(nums, target):
    flag, index = False, -1
    for i in range(len(nums)):
        if target == nums[i]:
            flag = True
            index = i
            break
    return flag, index
flag,index= linersearch(nums, target)
if flag:
    print(f"{target} Element found at index", index)
else:
    print(f"{target} Element not found in the list")
    '''

#Optimized code
'''
def createintlist():
    l = []
    while True:
        try:
            n = int(input("Enter the number "))
            l.append(n)
        except ValueError:
            return l
nums= createintlist()
target = int(input("Enter the number to search: "))
def linersearch(nums, target):
    for i in range(len(nums)):
        if target == nums[i]:
           return True, i
    return False, -1
flag,index= linersearch(nums, target)
if flag:
    print(f"{target} Element found at index", index)
else:
    print(f"{target} Element not found in the list")
    '''

#Write a program to display the largest element along with its index in the list 

def createintlist():
    l = []
    while True:
        try:
            n = int(input("Enter the number "))
            l.append(n)
        except ValueError:
            return l
nums= createintlist()

def find_largest(nums):
    max=-2**31
    max_index = -1
    for i in range(len(nums)):
        if max < nums[i]:
            max = nums[i]
            max_index = i
    return max, max_index
max_value, max_index = find_largest(nums)

if max_index != -1:
    print(f"Max element is {max_value} at index {max_index}")
else:
    print("list is empty")

# Write a program to display the smallest element along with its index in the list
def findmin(nums):
    min = 2**31
    min_index = -1
    for i in range(len(nums)):
        if min > nums[i]:
            min = nums[i]
            min_index = i
    return min, min_index

min_value, min_index = findmin(nums)
if min_index != -1:
    print(f"Min element is {min_value} at index {min_index}")
else:
    print("list is empty")


# Write a program to find the smallest and largest along with index character in a given array 

def createcharlist():
    char = []
    while True:
        n = input("Enter the char ")
        if n == "":
            return char
        char.append(n)
chars = createcharlist()
def find_largest_char(chars):
    max_char = ''
    max_index = -1
    for i in range(len(chars)):
        if max_char < chars[i]:
            max_char = chars[i]
            max_index = i
    return max_char, max_index
max_char, max_index = find_largest_char(chars)

