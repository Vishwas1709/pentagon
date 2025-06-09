'''
s1={1,2,3,4}
s2={3,4,5,6}

s3=s1.union(s2)
print(s3)  # Output: {1, 2, 3, 4, 5, 6}
s4=s1.intersection(s2)
print(s4)  # Output: {3, 4}
s5=s1.difference(s2)
print(s5)  # Output: {1, 2}
s6=s2.difference(s1)
print(s6)  # Output: {5, 6}
s7=s1.symmetric_difference(s2)
print(s7)  # Output: {1, 2, 5, 6}

s3={5,6,7,8}
print(s1.isdisjoint(s3))  # Output: True (s1 and s3 have no elements in common)
print(s1.isdisjoint(s2))  # Output: False (s1 and s2 have elements in common)
print(s1.isdisjoint(s3))  # Output: True (s1 and s3 have no elements in common)
print(s2.isdisjoint(s3))  # Output: False (s2 and s3 have elements in common)

s4={1,2,3,4}
s5={1,2}
print(s4.issubset(s5))  # Output: False (s4 is not a subset of s5)
print(s4.issuperset(s5))  # Output: True (s4 is a superset of s5)
print(s5.issuperset(s4))  # Output: False (s5 is not a superset of s4)
print(s5.issubset(s4))  # Output: True (s5 is a subset of s4)
'''
'''
#Frozenset
s1 = frozenset([1, 2, 3, 4])
print(s1)  # Output: frozenset({1, 2, 3, 4})
s1.add(5)  # Raises AttributeError: 'frozenset' object has no attribute 'add'
s1.discard(2)  # Raises AttributeError: 'frozenset' object has no attribute 'discard'
s1.remove(3)  # Raises AttributeError: 'frozenset' object has no attribute 'remove'
'''
'''
s1={10,20,30,[40,50],60}  # Raises TypeError: unhashable type: 'list'
print(s1)  # This line will not execute due to the error above
s2={10,20,30,(40,50),60}  # This is valid because tuples are hashable
print(s2)  # Output: {10, 20, 30, (40, 50), 60}
s3={10,20,30,{40,50},60}  # Raises TypeError: unhashable type: 'set'
print(s3)  # This line will not execute due to the error above
'''