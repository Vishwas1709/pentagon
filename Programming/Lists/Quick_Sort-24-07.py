def quick_sort(arr,left,right):
    if left>=right:
        return
    
    start,end=left,right
    mid=(start+end)//2
    pivot=arr[mid]

    while start<=end:
        #left part of pivot
        while arr[start]<pivot:
            start+=1
        #right part of pivot
        while arr[end]>pivot:
            end-=1
        if start <= end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1

    #LHS
    quick_sort(arr,left,end)

    #RHS
    quick_sort(arr,start,right)
    
    

arr=[2,5,6,1,3]
print("Original array is ",arr)
quick_sort(arr,0,len(arr)-1)
print("Asc Sorted array is ",arr)

