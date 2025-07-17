'''def decstring_reverse(s1):
    nstr=""
    for i in range((len(s1)-1),0-1,-1):
        nstr=nstr+s1[i]
    return nstr'''


'''def incre_string_rev(s1):
    nstr=""
    for i in range (len(s1)):
        nstr=s1[i]+nstr
    return nstr

s1=input("Enter the string")
print(f"Original string is {s1}")
# res=decstring_reverse(s1)
res=incre_string_rev(s1)
print(f"Reversed string is {res}")'''

#Using recursion 

'''def dec_string_reversal_recu(s1,nstr,i):
    if i<0:
        return nstr
    nstr=nstr+s1[i]
    return dec_string_reversal_recu(s1,nstr,i-1)

s1=input("Enter the string")
print(f"Original string is {s1}")

nstr=""
i=len(s1)-1
res=dec_string_reversal_recu(s1,nstr,i)
print(f"Reversed string is {res}")'''

#recursion incrementing loop

'''def inc_str_rev_rec(s1,nstr,i):
    if i==len(s1):
        return nstr
    nstr=s1[i]+nstr
    return inc_str_rev_rec(s1,nstr,i+1)
s1=input("Enter the string")
print(f"Original string is {s1}")
res=inc_str_rev_rec(s1,nstr="",i=0)
print(f"Reversed string is {res}")'''

# Using list reverse the string

def str_rev_unsing_list(s1):
    # string to list
    l1=[]
    for i in s1:
        l1.append(i)
    #l1=list(s1)  #It is the inbuilt function it can be directly convert the string to list
    #reverse the list
    i,j=0,len(l1)-1
    while i<j:
        l1[i],l1[j]=l1[j],l1[i]
        i+=1
        j-=1

    #list to string
    nstr=""
    for i in l1:
        nstr=nstr+i
    return nstr
    #nstr="".join(l1) It is a inbulit function it is directly converst the list to string 

s1=input("enter the string ")
print(f"Original string is {s1}")
res=str_rev_unsing_list(s1)
print(f"Reversed string is {res}")

