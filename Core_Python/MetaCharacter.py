import re
text="Python is easy"
regex=r"Python|easy"  # pipe matacharacter
res1=re.findall(regex,text)
print(res1)
# Output: ['Python', 'easy']

regex1=r"p*ython" # star matacharacter
res2=re.findall(regex1,text)
print(res2)
# Output: ['ython']    

text1="python is easy ppython ppppppython "
regex2=r"p+ython" # plus matacharacter
res3=re.findall(regex2,text1)
print(res3)
# Output: ['python','ppython', 'pppppython']

text2="python is easy ppython ppppppython "
regex3=r"p?ython" # question mark matacharacter matches 0 or 1 occurrence
res4=re.findall(regex3,text2)
print(res4)
# Output: ['ython', 'ppython', 'pppppython']

text3="python is super easy"
regex4=r"^python"  # caret matacharacter matches the start of the string
res5=re.findall(regex4,text3)
print(res5)
# Output: ['python']

res6=re.findall(r"easy$",text3)  # dollar matacharacter matches the end of the string
print(res6)
# Output: ['easy']
res7=re.search(r"easy$",text3)  # search for the end of the string
print(res7)

