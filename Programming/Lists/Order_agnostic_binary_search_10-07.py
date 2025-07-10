def createlist():
    l=[]
    while True:
        try:
            n=int(input("Enter the number "))
            l.append(n)
        except Exception as e:
            return l
def order_agnostic_binary_search(arr,tar):
    left=0
    right=len(arr)-1
    flag=True       #Ascending
    if arr[left]>arr[right]:
        flag=False   #decending
    while left<=right:
        mid=(left+right)//2
        if tar==arr[mid]:
            return mid
        if flag:        #Ascending
            if tar<arr[mid]:
                right=mid-1
            else:
                left=mid+1
        else:           #Decending
            if tar<arr[mid]:
                left=mid+1
            else:
                right=mid-1
    return -1
nums=createlist()
print(f"Original Array is {nums}")
tar=int(input("Enter a element to search"))
res=order_agnostic_binary_search(nums,tar)
if res==-1:
    print(f"{tar} is not found in the list")
else:
    print(f"{tar} is found at the index at {res}")




