# import re
# text="Python is easy"
# regex=r"Python"
# res1=re.match(regex,text)
# print(res1)


import re
text="Python is easy"
regex=r"easy"
res1=re.search(regex,text)
print(res1)