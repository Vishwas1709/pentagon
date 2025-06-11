import pickle
class Employee:
    def __init__(self,name,age,ph_num,addr):
        self.name=name
        self.age=age
        self.ph_num=ph_num
        self.addr=addr
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Phone Number:",self.ph_num)
        print("Address:",self.addr)

# Serialization: Writing an object to a file
# e=Employee("Rama",25,1234567890,"India")
# f=open("emp.txt","wb")  # Open file in write binary mode
# pickle.dump(e,f)  # Serialize the object and write it to the file
# print("Details are inserted into the file")
# f.close()  # Close the file


# Deserialization: Reading an object from a file

f=open("emp.txt","rb")  # Open file in read binary mode
e=pickle.load(f)  # Deserialize the object from the file
e.display()  # Display the employee details
print("Details are read from the file")
f.close()  # Close the file
