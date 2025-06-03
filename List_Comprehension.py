a=[10,20,30,40,50]
b=[]
c=[]
for data in a:
    new_data=data+1
    b.append(new_data)
print(b)

for data1 in a:
    new_data1=data1*data1
    c.append(new_data1)
print(c)

x=["apple", "banana", "cherry"]
d=[]
for data2 in x:
    new_data2=data2.upper()
    d.append(new_data2)
print(d)


y="abc123def456"
p=[]
q=[]
for data3 in y:
    if data3.isdigit():
        p.append(data3)
print(p)

for data4 in y:
    if data4.isalpha():
        q.append(data4)
print(q)


z=range(5,20)
r=[]
v=[]

for data5 in z:
    if data5%2==0:
        r.append(data5)
    else:
        v.append(data5)
print(r)
print(v)