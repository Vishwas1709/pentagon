'''
def countdigit(n,count):
    if n<=0:
        return count
    n=n//10
    count+=1
    return countdigit(n,count)
n=int(input("Enter a number"))
res=countdigit(n,0)
print(res)
'''


def countdigit(n,count):
    if n<=0:
        return count
    n=n//10
    count+=1
    return countdigit(n,count)

def isasn(n,pow,asn,temp):
    if n<=0:
        return asn==temp
    base=n%10
    asn=asn+(base**pow)
    n=n//10
    return isasn(n,pow,asn,temp)
n=int(input("Enter a number: "))
pow=countdigit(n,0)
temp=n
asn=0
flag=isasn(n,pow,asn,temp)
if flag:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
# Vishwas Chandra M C