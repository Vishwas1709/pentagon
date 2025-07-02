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



