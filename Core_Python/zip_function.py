
# names=["Kohli","ABD","Rohit","Dhoni"]
# runs=[9000, 8000, 7000, 6000]
# country=["IND","SA","IND","IND"]
# ipl_teams=["RCB","RCB","Mumbai","CSK"]
# c_info=list(zip(names,runs,country,ipl_teams))
# print(c_info)
# This code snippet creates a list of tuples using the zip function

from itertools import zip_longest
names=["Kohli","ABD","Rohit","Dhoni"]
runs=[9000, 8000, 7000, 6000]
country=["IND","SA","IND","IND"]
ipl_teams=["RCB","RCB"]
c_info=list(zip_longest(names,runs,country,ipl_teams,fillvalue="#"))
print(c_info)
    