'''
def createlist():
    arr=[]
    while True:
        try:
            n = int(input("Enter the number "))
            arr.append(n)
        except ValueError:
            return arr
print("Enter values into first list")
nums1=createlist()
print("Enter values into second list")
nums2=createlist()
print("Original array 1:", nums1)
print("Original array 2:", nums2)
nums1.extend(nums2)
print("Merged array:", nums1)
a=sorted(nums1)
print("Sorted array:", a)
'''
# by using the concantinate the two array
'''
def createlist():
    arr=[]
    while True:
        try:
            n = int(input("Enter the number "))
            arr.append(n)
        except ValueError:
            return arr
print("Enter values into first list")
nums1=createlist()
print("Enter values into second list")
nums2=createlist()
print("Original array 1:", nums1)
print("Original array 2:", nums2)
res=nums1+nums2
print("Merged array:", res)


a=sorted(nums1)
print("Sorted array:", res)
'''

#By using the append function we can add the two array the first original array will go on
'''def createlist():
    arr=[]
    while True:
        try:
            n = int(input("Enter the number "))
            arr.append(n)
        except ValueError:
            return arr
print("Enter values into first list")
nums1=createlist()
print("Enter values into second list")
nums2=createlist()
print("Original array 1:", nums1)
print("Original array 2:", nums2)

for i in range (len(nums2)):
    nums1.append(nums2[i])

print("Merged array:", nums1)'''

'''def createlist():
    arr=[]
    while True:
        try:
            n = int(input("Enter the number "))
            arr.append(n)
        except ValueError:
            return arr
print("Enter values into first list")
nums1=createlist()
print("Enter values into second list")
nums2=createlist()
print("Original array 1:", nums1)
print("Original array 2:", nums2)

for i in range (len(nums2)):
    nums1.insert(len(nums1),nums2[i])

print("Merged array:", nums1)'''


#write a program to merge the given 2 ascending sorted array in sorted order

'''def createlist():
    arr=[]
    while True:
        try:
            n = int(input("Enter the number "))
            arr.append(n)
        except ValueError:
            return arr
print("Enter values into first list")
nums1=createlist()
print("Enter values into second list")
nums2=createlist()
print("Original array 1:", nums1)
print("Original array 2:", nums2)

n1=len(nums1)
n2=len(nums2)
res=[]
i=0
j=0
while i<n1 and j<n2:
    if nums1[i]<nums2[j]:
        res.append(nums1[i])
        i+=1
    else:
        res.append(nums2[j])
        j+=1
while i<n1:
    res.append(nums1[i])
    i+=1
while j<n2:
    res.append(nums2[j])
    j+=1
print("Merged array in sorted order:", res)'''

#By using function

'''def merge_sorted_arrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    res = []
    i = 0
    j = 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    while i < n1:
        res.append(arr1[i])
        i += 1
    while j < n2:
        res.append(arr2[j])
        j += 1
    return res

def createlist():
    arr=[]
    while True:
        try:
            n = int(input("Enter the number "))
            arr.append(n)
        except ValueError:
            return arr
print("Enter values into first list")
nums1=createlist()
print("Enter values into second list")
nums2=createlist()
print("Original array 1:", nums1)
print("Original array 2:", nums2)
res= merge_sorted_arrays(nums1, nums2)
print("Merged array in sorted order:", res)
'''

#write a program to merge the given 2 sorted descending order array in sorted order

'''def merge_sorted_descending(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    res = []
    i = 0
    j = 0
    while i < n1 and j < n2:
        if arr1[i] > arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    while i < n1:
        res.append(arr1[i])
        i += 1
    while j < n2:
        res.append(arr2[j])
        j += 1
    return res
def createlist():
    arr=[]
    while True:
        try:
            n = int(input("Enter the number "))
            arr.append(n)
        except ValueError:
            return arr
print("Enter values into first list")
nums1=createlist()
print("Enter values into second list")
nums2=createlist()
print("Original array 1:", nums1)
print("Original array 2:", nums2)
res= merge_sorted_descending(nums1, nums2)
print("Merged array in sorted order:", res)
'''



#Write a program to merge the given 2 sorted decending lists in ascending sorted order

def merge_sorted_ascending(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    res = []
    i = 0
    j = 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    while i < n1:
        res.append(arr1[i])
        i += 1
    while j < n2:
        res.append(arr2[j])
        j += 1
    return res
def createlist():
    arr=[]
    while True:
        try:
            n = int(input("Enter the number "))
            arr.append(n)
        except ValueError:
            return arr
print("Enter values into first list")
nums1=createlist()
print("Enter values into second list")
nums2=createlist()
print("Original array 1:", nums1)
print("Original array 2:", nums2)
res= merge_sorted_ascending(nums1, nums2)
print("Merged array in sorted order:", res)

