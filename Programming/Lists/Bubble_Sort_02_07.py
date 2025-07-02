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

def bubble_sort_inc(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort_inc(nums)
print("Sorted increasing array:", nums)

def bubble_sort_dec(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort_dec(nums)
print("Sorted decresing array:", nums)