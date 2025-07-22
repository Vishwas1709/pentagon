def createarrray():
    arr=[]
    while True:
        try:
            n=int(input("Enter a number "))
            arr.append(n)
        except Exception as e:
            break
    return arr

def display_array(arr):
    dict={}
    duplicate_elements = []
    unique_elements = []
    non_duplicate_elements = []
    for i in range(len(arr)):
        if arr[i] in dict:
            dict[arr[i]] = dict[arr[i]] + 1
        else:
            dict[arr[i]] = 1
    # for key in dict:
    #     if dict[key]>1:
    #         duplicate_elements.append(key)
    #     if dict[key]==1:
    #         unique_elements.append(key)
    #     if dict[key]>=1:
    #         non_duplicate_elements.append(key)

# we can use any type of these two methods
    for key,values in dict:
        if values>1:
            duplicate_elements.append(key)
        if values==1: 
            unique_elements.append(key)
        if values>=1:
            non_duplicate_elements.append(key)

    return [duplicate_elements,unique_elements,non_duplicate_elements]
        
arr=createarrray()
res =display_array(arr)
print(f" The array is {arr}")
print(f" Duplicated elements are {res[0]}")
print(f" Unique elements are {res[1]}")
print(f" Non Duplicated elements are {res[2]}")

