# WPP to reverse the number using recursion
'''
def revnum(n,rev):
    if n<=0:
        return rev
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
    return revnum(n,rev)
n=int(input("Enter the number"))
rev=0
res=revnum(n,rev)
print("The reversed number is ",res)

#WPP to print palindrome using recursion


def ispalindrome(n,rev,temp):
    if n<=0:
        return temp==rev
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
    return ispalindrome(n,rev,temp)
n=int(input("Enter the number"))
rev=0
temp=n
flag=ispalindrome(n,rev,temp)
if flag:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")
    '''

# WPP to factors of a number using recursion

def factor(i,n):
    if i>n:
        return 
    if n%i==0:
        print(i,end=" ")
    i+=1
    factor(i,n)
n=int(input("Enter a number"))
factor(1,n)

      
    