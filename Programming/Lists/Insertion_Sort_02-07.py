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

def insertion_sort_asc(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range((i+1),0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

insertion_sort_asc(nums)
print("Sorted Incresing array:", nums)

def insertion_sort_dec(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range((i+1),0,-1):
            if arr[j] > arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                
insertion_sort_dec(nums)
print("Sorted Decreasing array:", nums)
        






































