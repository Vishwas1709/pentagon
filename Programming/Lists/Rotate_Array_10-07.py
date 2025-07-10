#Write a program to rotate a given array to lhs for k number of times

def createlist():
    l=[]
    while True:
        try:
            n=int(input("Enter the number "))
            l.append(n)
        except Exception as e:
            return l
        
def reverse_list(i,j,arr):
    while i<=j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

def rotate_left(arr,k):
    n=len(arr)
    if k >= n:
        k = k % n
    reverse_list(0,(k-1),arr)
    reverse_list(k,(n-1),arr)
    reverse_list(0,(n-1),arr)

nums=createlist()
print(f"Original List is {nums}")
k=int(input("Enter the number of times to rotate"))
rotate_left(nums,k)
print(f"Rotated Array {nums}")