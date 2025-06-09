# def fun1():
#     print("I am outer function")
#     def fun2():
#         print("I am inner function")
#         print(fun2)
#     return fun2  # Return the inner function without calling it
# ref1=fun1()  # Call the outer function and get the reference to the inner function
# print(ref1)  # This will print the memory address of the inner function
# ref1()  # Call the inner function using the reference


#Control flow of Closures functions

def outer():
    print("Entering Outer")
    def inner():
        print("Entering Inner")
        print("Processing")
        print("Leaving Inner")
    print("Calling Inner")
    return inner  # Return the inner function without calling it
ref1=outer()  # Call the outer function and get the reference to the inner function
print("After Executing Outer")
ref1()  # Call the inner function using the reference
print("After Executing Inner")


