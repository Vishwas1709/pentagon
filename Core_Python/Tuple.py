'''
t=(10,20,30,40)
t1=(10,20.2,"Rama")
t2=()
print(t)
print(t1)
print(type(t))
print(type(t1))
t4=(10)
print(type(t4))  # This will print <class 'int'>, not a tuple
t5=(10,)  # Adding a comma makes it a tuple
print(type(t5))  # This will print <class 'tuple'>
# Tuples are immutable, so we cannot change their elements


a=(10,20,30,40,50,60)
print(a)
print(len(a))
print(a[1])
print(a[3])
print(a[5])
print(a[-1])  # Accessing the last element
print(a[-2])  # Accessing the second last element
print(a[0:2])  # Slicing from index 0 to 1
print(a[3:5])  # Slicing from index 3 to 4
print(a[ :3])  # Slicing from start to index 2
print(a[3:])  # Slicing from index 3 to the end
print(a[ : : -1])
print(a[ -5 : -2])  # Slicing from index -5 to -3
print(a[-5:-2:-1])  # No elements will be returned as the step is negative and the start index is less than the end index
print(a[4:0:-1])  # Slicing from index 4 to 1 in reverse order
print(a[0:2:-1])  # No elements will be returned as the step is negative and the start index is less than the end index
print(a[:])  # Slicing the entire tuple
#print(a[0:3:0])  # This will raise an error as the step cannot be zero
'''
'''
#Insertion and Deletion

a=(10,20,30,40,50,60)
# Tuples are immutable, so we cannot insert or delete elements
# However, we can convert a tuple to a list, modify it, and then convert it back to a tuple
b=a[0:2] + (25,) + a[2:]  # Inserting 25 at index 2
print(b)  # Output: (10, 20, 25, 30, 40, 50, 60)
c=a[0:2] + a[3:]
print(c)  # Output: (10, 20, 40, 50, 60)
# Deleting elements is not possible directly, but we can create a new tuple without the element we want to delete

# List in tuple:

stud_info=("Rama",[40,50,60])
name,ia_marks=stud_info
print(name)  # Output: Rama
print(ia_marks)  # Output: [40, 50, 60]
'''

a=(10,20,30,(10.1,20.2,("A","B","C"),30.3),40,50)
print(a)
print(a[2])  # Accessing the third element
print(len(a))  # Length of the tuple
print(a[3][3])  # Accessing the fourth element of the nested tuple
print(a[3][2][2])  # Accessing the third element of the nested tuple inside the fourth element
print(a[3][2])
print(a[3])