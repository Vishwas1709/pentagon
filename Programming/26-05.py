def countdigit(n):
    count=0
    while n>0:
        n//=10
        count+=1
    return count

def isarmstrong(a,b):
    asn=0
    temp=b
    pow=a
    while temp>0:
        base=temp%10
        asn=asn+(base**pow)
        temp//=10
    return asn

n=int(input("Enter a number: "))
temp=n
asn=0
pow =countdigit(n)
res=isarmstrong(pow,temp)
if res==temp:
    print(f"{temp} is an Armstrong number")
else:
    print(f"{temp} is not an Armstrong number")
    
    