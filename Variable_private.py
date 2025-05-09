class Book:
    def __init__(self,value):
        self.__pages = value
b1=Book(100)
print(b1.__pages) # AttributeError: 'Book' object has no attribute '__pages'