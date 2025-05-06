def fun1():
    a=10
    print("From fun1 a",a)
    def fun2():
        nonlocal a  # This allows us to modify the variable 'a' from the outer function
        a=100
        b=20
        print("From fun2 b",b)
        print("From fun2 a",a)
    fun2()
    print("From fun1 a",a)  # This will now print the modified value of 'a'
fun1()
print("End of program")