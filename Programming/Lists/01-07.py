''''\nWrite a program to find the maximum and second maximum element in an array and their indices.\n
def createlist():
    arr=[]
    while True:
        try:
            n = int(input("Enter the number "))
            arr.append(n)
        except ValueError:
            return arr
nums=createlist()

def max(arr):
    max=-2**31
    secmax=-2**31
    maxindex=-1
    secmaxindex=-1
    for i in range(len(nums)):
        if max<nums[i]:
            secmax=max
            secmaxindex=maxindex
            max=nums[i]
            maxindex=i
        elif max!=nums[i] and secmax<nums[i]:
            secmax=arr[i]
            secmaxindex=i
#     return max, secmax, maxindex, secmaxindex
# max_value, sec_max_value, max_index, sec_max_index = max(nums)
# print("Max value:", max_value)
# print("Second Max value:", sec_max_value)
# print("Max index:", max_index)
# print("Second Max index:", sec_max_index)
    return [max, secmax, maxindex, secmaxindex]
res=max(nums)
print(f"Max value: {res[0]} at index: {res[2]}")
print(f"Second Max value: {res[1]} at index: {res[3]}")
'''


#write a program to reverse the given array in place 


def createlist():
    arr=[]
    while True:
        try:
            n = int(input("Enter the number "))
            arr.append(n)
        except ValueError:
            return arr
nums = createlist()

def reverse_array(nums):
    i=0
    j=len(nums)-1
    while i<j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    
reverse_array(nums)
print("Reversed array:", nums)
