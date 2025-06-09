emp_info={"name":"Rama","age":30,"height":5.6,"address":"Mandya"}
print(emp_info)  # Output: {'name': 'Rama', 'age': 30, 'height': 5.6, 'address': 'Mandya'}
print(type(emp_info))  # Output: <class 'dict'>
print(emp_info["name"])  # Output: Rama
emp_info["Mobile"]="1234567890"  # Adding a new key-value pair
print(emp_info)  # Output: {'name': 'Rama', 'age': 30, 'height': 5.6, 'address': 'Mandya', 'Mobile': '1234567890'}
print("===================================================")
student_info = {"Name": "Rama","Age":22,"Height":5.6,"Address":"Mandya"}
print(student_info)  # Output: {'Name': 'Rama', 'Age': 22, 'Height': 5.6, 'Address': 'Mandya'}
print(student_info["Age"])  # Output: 22

for i in student_info:
    print(i)  # Prints the keys: Name, Age, Height, Address
for i in student_info:
    print(student_info[i])  # Prints the values: Rama, 22, 5.6, Mandya
for i in student_info.values():
    print(i)  # Prints the values: Rama, 22, 5.6, Mandya
for index,values in student_info.items():
    print(index,values)  # Prints key-value pairs: Name Rama, Age 22, Height 5.6, Address Mandya