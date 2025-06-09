# d={1:11,2:22,3:33,4:44}
# print(d)
# d1=d
# d[2]=222  # Modifying the value for key 2
# print(d)  # Output: {1: 11, 2: 222, 3: 33, 4: 44}
# print(d1)  # Output: {1: 11, 2: 222, 3: 33, 4: 44} (d1 reflects the change in d)
# d[2]=2222  # Further modifying the value for key 2
# print(d)  # Output: {1: 11, 2: 2222, 3: 33, 4: 44}
# print(d1)  # Output: {1: 11, 2: 2222, 3: 33, 4: 44} (d1 still reflects the change in d)
# d2=d.copy()  # Creating a shallow copy of d
# d[2]=21  # Modifying the value for key 2 in the original dictionary
# print(d)  # Output: {1: 11, 2: 21, 3: 33, 4: 44}
# print(d1)  # Output: {1: 11, 2: 2222, 3: 33, 4: 44} (d1 remains unchanged)
# print(d2)  # Output: {1: 11, 2: 2222, 3: 33, 4: 44} (d2 is a copy of d before the last modification)
# print("---------------------------------")
# student={"Name":"Rama","Age":22,"Ph_num":{"mob1":1234,"mob2":3456},"Address":{"Present":"Mandya","Permanent":"Bangalore"}}
# print(student)  # Output: {'Name': 'Rama', 'Age': 22, 'Ph_num': {'mob1': 1234, 'mob2': 3456}, 'Address': {'Present': 'Mandya', 'Permanent': 'Bangalore'}}
# print(student["Ph_num"]["mob1"])  # Output: 1234
# print(student["Address"]["Present"])  # Output: Mandya
# student["marks"]={1:80,2:90,3:95}  # Adding a new key 'marks' with a dictionary value
# print(student)  # Output: {'Name': 'Rama', 'Age': 22, 'Ph_num': {'mob1': 1234, 'mob2': 3456}, 'Address': {'Present': 'Mandya', 'Permanent': 'Bangalore'}, 'marks': {1: 80, 2: 90, 3: 95}}
# del(student["marks"])  # Deleting the 'marks' key from the dictionary
# print(student)  # Output: {'Name': 'Rama', 'Age': 22, 'Ph_num': {'mob1': 1234, 'mob2': 3456}, 'Address': {'Present': 'Mandya', 'Permanent': 'Bangalore'}}

# print("**********************************************************")
# student={"Name":"Rama","Age":22,"ph_num":{"mob1":1234,"mob2":3456},"Address":{"Present":"Mandya","Permanent":"Bangalore"}}
# print(student)
# s1=student 
# s1["ph_num"]["mob1"]=6666 # Modifying the value of 'mob1' in the nested dictionary
# print(student["ph_num"]["mob1"])  # Output: 6666
# print(s1["ph_num"]["mob1"])  # Output: 6666 (s1 reflects the change in student)

# s2=student.copy()  # Creating a shallow copy of student
# s1["Address"]["Present"]="Mysore"  # Modifying the 'Present' address in the nested dictionary
# print(student["Address"]["Present"])  # Output: Mysore
# print(s1["Address"]["Present"])  # Output: Mysore (s1 reflects the change in student)
# print(s2["Address"]["Present"])  # Output: Mysore (s2 is a shallow copy, so it reflects the change in student)
print("**********************************************************")

# import copy
# print("**********************************************************")
# student={"Name":"Rama","Age":22,"ph_num":{"mob1":1234,"mob2":3456},"Address":{"Present":"Mandya","Permanent":"Bangalore"}}
# print(student)
# s1=student 
# s1["ph_num"]["mob1"]=6666 # Modifying the value of 'mob1' in the nested dictionary
# print(student["ph_num"]["mob1"])  # Output: 6666
# print(s1["ph_num"]["mob1"])  # Output: 6666 (s1 reflects the change in student)

# s2=copy.deepcopy(student)  # Creating a shallow copy of student
# s1["Address"]["Present"]="Mysore"  # Modifying the 'Present' address in the nested dictionary
# print(student["Address"]["Present"])  # Output: Mysore
# print(s1["Address"]["Present"])  # Output: Mysore (s1 reflects the change in student)
# print(s2["Address"]["Present"])  # Output: Mysore (s2 is a shallow copy, so it reflects the change in student)


emp_id=[101,102,103,104]
emp_name=["Rama","Shyam","Sita","Gita"]
emp_ph=[1234,5678,9101,1121]
emp_address=["Mandya","Bangalore","Mysore","Chennai"]
info1=list(zip(emp_name, emp_ph,emp_address))
emp_det=dict(zip(emp_id, info1))
print(emp_det)  # Output: {101: ('Rama', 1234, 'Mandya'),
