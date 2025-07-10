def createlist():
    arr=[]
    while True:
        try:
            n = int(input("Enter the number "))
            arr.append(n)
        except ValueError:
            return arr
nums=createlist()
print("Original array:", nums)
tar=int(input("Enter the number to search: "))

'''def binary_search_ascending(nums,tar):
    left=0
    right=len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if tar==nums[mid]:
            return  mid
        elif tar>nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1
value= binary_search_ascending(nums, tar)
if value == -1:
     print(f"{tar} Element not found in the list")
else:
    print(f"{tar} Element found at index", value)'''

def binary_search_decending(nums,tar):
    left=0
    right=len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if tar==nums[mid]:
            return  mid
        elif tar<nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1
value= binary_search_decending(nums, tar)
if value == -1:
     print(f"{tar} Element not found in the list")
else:
    print(f"{tar} Element found at index", value)
    
