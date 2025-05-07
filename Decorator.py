# def Outer(function):
#     print("I am outer function")
#     def inner():
#         print("I am inner function")
#     return inner # Return the inner function without calling it
# ref1=Outer(1)  # Call the outer function and get the reference to the inner function
# print(ref1)  # This will print the memory address of the inner function
# ref1()  # Call the inner function using the reference


#Control flow of Decorator functions
#Defination 1
# def print_msg():
#     print("Hello EveryOne")
# def Outer(print1):
#     print("Entering Outer")
#     def inner():
#         print("Entering Inner")
#         ref =print1
#         ref()
#         print("Leaving Inner")
#     print("Calling Inner")
#     return inner  # Return the inner function without calling it
# ptr1=print_msg  # Assign the function to a variable
# ptr2=Outer(ptr1)  # Call the outer function and get the reference to the inner function
# ptr2()  # Call the inner function using the reference
# print("Program Ended")

#Definition 2

def print_msg():
    msg="Hello EveryOne"
    return msg
def Outer(print1):
    print("Entering Outer")
    def inner():
        print("Entering Inner")
        ref =print1
        res=ref()
        res1=res.upper()
        print(res1)
        print("Leaving Inner")
    return inner  # Return the inner function without calling it
ptr1=print_msg  # Assign the function to a variable
ptr2=Outer(ptr1)  # Call the outer function and get the reference to the inner function
ptr2()  # Call the inner function using the reference
print("Program Ended")
#In the above code, the outer function is called first, and it returns the inner function. The inner function is then called, which in turn calls the original function passed to it. This allows for additional functionality to be added before or after the original function is executed.

