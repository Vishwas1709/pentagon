'''l1=[]
l1.append(10)
print(l1)
l1.append(-5)
print(l1)
l1.append("abc")
print(l1)
l1.insert(1,100)
print(l1)
l1.insert(5,200)
print(l1)
l1[4]=555
#l1[8]=666 #error

l2=[-2,-3]
l1.extend(l2)
print(l1)
'''

'''

val=input("Enter the value")
print(val)
print(type(val))

print("--------------------------------------")
try:
    val = int(input("Enter the number"))
    print(val)
    print(type(val))
except Exception as e:
    print("Invalid Input")
'''

#write a program to create dynamic integer array without asking thr length from the user 
'''
l=[]
while True:
    try:
        n=int(input("Enter the number"))
        l.append(n)
    except Exception as e:
        break
print(l)
'''
# using function
'''
def createintlist():
    l=[]
    while True:
        try:
            n=int(input("Enter the number"))
            l.append(n)
        except Exception as e:
            return l
res=createintlist()
print(res)
'''

#write a program to create dynamic character array without asking thr length from the user 
'''
l=[]
while True:
        n=(input("Enter the char"))
        if n=="":
            break
        l.append(n)
print(l)
'''
#using function

def createcharlist():
      char=[]
      while True:
            n=input("Enter a character: ")
            if n=="":
                  return char
            char.append(n)
res=createcharlist()
print(res)