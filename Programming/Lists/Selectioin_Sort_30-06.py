# def createlist():
#     arr=[]
#     while True:
#         try:
#             n = int(input("Enter the number "))
#             arr.append(n)
#         except ValueError:
#             return arr
        
# arr = createlist()
# print("Original array:", arr)

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(0,n-1):
#         max=-2**31
#         currentmaxindex=-1
#         for j in range(0,n-i):
#             if max<arr[j]:
#                 max=arr[j]
#                 currentmaxindex=j
#         arr[currentmaxindex], arr[n-1-i] = arr[n-1-i], arr[currentmaxindex]#n-1-i is the actual_index 
#     return arr
# sorted_arr = selection_sort(arr)
# print("Sorted array:", sorted_arr)


# def selection_sort_desending(arr):
#     n=len(arr)
#     for i in range(0,n-1):
#         min=2**31
#         currentminindex=-1
#         for j in range(0,n-i):
#             if min>arr[j]:
#                 min=arr[j]
#                 currentminindex=j
#         arr[currentminindex], arr[n-1-i] = arr[n-1-i], arr[currentminindex]#n-1-i is the actual_index
#     return arr
# decending_arr=selection_sort_desending(arr)
# print("Decending array:", decending_arr)


# we dont need the return statement because we can change the memory in the same array function 

def createlist():
    arr=[]
    while True:
        try:
            n = int(input("Enter the number "))
            arr.append(n)
        except ValueError:
            return arr
        
arr = createlist()
print("Original array:", arr)

def selection_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        max=-2**31
        currentmaxindex=-1
        for j in range(0,n-i):
            if max<arr[j]:
                max=arr[j]
                currentmaxindex=j
        arr[currentmaxindex], arr[n-1-i] = arr[n-1-i], arr[currentmaxindex]#n-1-i is the actual_index 


def selection_sort_desending(arr):
    n=len(arr)
    for i in range(0,n-1):
        min=2**31
        currentminindex=-1
        for j in range(0,n-i):
            if min>arr[j]:
                min=arr[j]
                currentminindex=j
        arr[currentminindex], arr[n-1-i] = arr[n-1-i], arr[currentminindex]#n-1-i is the actual_index

selection_sort(arr)
print("Sorted array:",arr)
selection_sort_desending(arr)
print("Decending array:",arr)