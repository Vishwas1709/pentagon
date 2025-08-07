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
print("Original array 1:", nums1)
print("Enter values into second list")
nums2=createlist()
print("Original array 2:", nums2)

def merge_alternate(nums1,nums2):
    res=[]
    n1=len(nums1)
    n2=len(nums2)
    n3=n1+n2
    i=0
    j=0
    k=0
    while k<n3:
        if i<n1 and k%2==0:
            res.append(nums1[i])
            i+=1
        elif j<n2 and k%2!=0:
            res.append(nums2[j])
            j+=1
        else:
            if i<n1:
                res.append(nums1[i])
                i+=1
            elif j<n2:
                res.append(nums2[j])
                j+=1
        k+=1
    return res
merged_list = merge_alternate(nums1, nums2)
print("Merged array in alternate order:", merged_list)
