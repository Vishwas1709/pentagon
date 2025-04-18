str="RajaRamMohanRoy"
print(str)
print(str[0])  # First character
print(str[1])  # Second character
print(str[7])  # Eighth character
print(str[-1])  # Last character
print(str[-6]) # Sixth character from the end
print(str[0:4])  # First four characters
print(str[4:7])  # Characters from index 4 to 6
print(str[0:])  # All characters from index 0 to end
print(str[:4])  # All characters from start to index 3
print(str[::2])  # All characters with a step of 2
print(str[7:])  # All characters from index 7 to end
print(str[ :7])
print(str[ :])  # All characters from start to end
print(str[: : -1])  # All characters in reverse order
print(str[ : : 1])  # All characters in original order
print(str[9:3])  # Empty string (invalid range)
print(str[3:9:-1])  # Empty string (invalid range)
print(str[9:3:-1])  # Empty string (invalid range)
print(str[ : 10:-1])  # Empty string (invalid range)
print(str[-5: : -1])
print(str[-8: -3])  # Characters from index -8 to -4 (exclusive)
print(str[-4:-9:-1])
print(str[ : : 3])  # All characters with a step of 3
# print(str[5:12:0])  # Empty string (invalid step)
