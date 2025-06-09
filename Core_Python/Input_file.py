# print("Enter the file name")
# fname=input()
# fptr=open(fname,"a")
# for i in range (5):
#     print("Enter the name ")
#     data=input()
#     #fptr.write(data) #  in same line 
#     fptr.write(data +"\n") # In next line
# fptr.close()
# print("5 names are written to file")

print("Enter the file name")
fname=input()
fptr=open(fname,"a")
for i in range (5):
    eid=input("Enter the eid")
    name=input("enter the eanme")
    role=input("enter the role")
    mob=input("Enter the mobile number")
    addr=input("Enter the address")
    fptr.write (eid+"\t"+name+"\t"+ role +"\t"+mob+"\t"+addr+"\n")
fptr.close()
print(" 5 rows are inserted")
