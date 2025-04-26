class Demo:
    def disp(self,a,b):  # formal parameters
        temp=a
        a=b
        b=temp

d1=Demo()
x=100
y=200
print("Before swapping: x=",x,"y=",y)
d1.disp(x,y)  # actual parameters  (Arguments)
print("After swapping: x=",x,"y=",y)
# Output:
# Before swapping: x= 100 y= 200
# After swapping: x= 100 y= 200
# The values of x and y are not swapped because the function only swaps the local copies of the variables.
# To swap the values of x and y, we need to return the swapped values from the function and assign them back to x and y.
