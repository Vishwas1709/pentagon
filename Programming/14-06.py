def happynum(n):
    sum=0
    if n==1:
        return True
    elif n==4:
        return False
    while n>0:
        rem=n%10
        sum=sum+(rem*rem)
        n=n//10
    return happynum(sum)
n=int(input("Enter the number"))
res=happynum(n)
if res:
    print(f"{n} is a Happy number")
else:
    print(f"{n} is Not Happy Number")
     