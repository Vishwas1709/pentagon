def fun1(a=50,b=60,c=70):
    print(a,b,c)
x=11
y=22
z=33
fun1(x,y,z) # 11 22 33
fun1(x,y) # 11 22 70
fun1(x) # 11 60 70
fun1(z) # 33 60 70
fun1() # 50 60 70
fun1(c=z) # 50 60 33 #Keyword argument
fun1(b=y,c=z) # 50 22 33 #Keyword argument