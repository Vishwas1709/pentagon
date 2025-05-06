# def Outer(function):
#     print("I am outer function")
#     def inner():
#         print("I am inner function")
#     return inner # Return the inner function without calling it
# ref1=Outer(1)  # Call the outer function and get the reference to the inner function
# print(ref1)  # This will print the memory address of the inner function
# ref1()  # Call the inner function using the reference


#Control flow of Decorator functions

def print_msg():
    print("Hello EveryOne")
def Outer(print1):
    print("Entering Outer")
    def inner():
        print("Entering Inner")
        ref =print1
        ref()
        print("Leaving Inner")
    print("Calling Inner")
    return inner  # Return the inner function without calling it
ptr1=print_msg  # Assign the function to a variable
ptr2=Outer(ptr1)  # Call the outer function and get the reference to the inner function
ptr2()  # Call the inner function using the reference
print("Program Ended")
