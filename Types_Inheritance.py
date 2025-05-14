# # Single Inheritance

# # class A:
# #     def dispA(self):
# #         print("Inside dispA")
# # class B(A):
# #     def dispB(self):
# #         print("Inside dispB")
# # b=B()
# # b.dispB()
# # b.dispA()


# # Multi-Level Inheritance

# class A:
#     def dispA(self):
#         print("Inside dispA")
# class B(A):
#     def dispB(self):
#         print("Inside dispB")
# class C(B):
#     def dispC(self):
#         print("Inside dispC")
# c=C()
# c.dispC()
# c.dispB()
# c.dispA()

# Hierarchical Inheritance
# class A:
#     def dispA(self):
#         print("Inside dispA")
# class B(A):
#     def dispB(self):
#         print("Inside dispB")
# class C(A):
#     def dispC(self):
#         print("Inside dispC")
# c=C()
# b=B()
# c.dispC()
# c.dispA()
# b.dispB()
# b.dispA()


#Multiple Inheritance
class A:
    def dispA(self):
        print("Inside dispA")
class B:
    def dispB(self):
        print("Inside dispB")
class C(A,B):
    def dispC(self):
        print("Inside dispC")
c=C()
c.dispC()
c.dispB()
c.dispA()






