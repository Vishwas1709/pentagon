def createlist():
    l=[]
    while True:
        try:
            n=int(input("Enter the number "))
            l.append(n)
        except Exception as e:
            return l


def merge(arr, left, mid, right):
    res=[]
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[j])
            j += 1
    while i <= mid:
        res.append(arr[i])
        i += 1
    while j <= right:
        res.append(arr[j])
        j += 1  
    for k in range(len(res)):
        arr[left] = res[k]
        left += 1

def merge_sort_breaking(arr,left, right):
    if left==right:
        return
    mid=(left+right)//2
    #firsrt array
    merge_sort_breaking(arr, left, mid)
    #Second Array
    merge_sort_breaking(arr, mid+1, right)
    #merge the arrays
    merge(arr, left, mid, right)

arr=createlist()
print(f"Original List is {arr}")
merge_sort_breaking(arr, 0, len(arr) - 1)
print(f"Sorted List is {arr}")