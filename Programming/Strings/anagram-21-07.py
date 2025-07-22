def anagramfiltrations(s1):
    nstr=""
    for i in range(len(s1)):
        if "A" <= s1[i] <="Z":
            nstr=nstr+chr(ord(s1[i])+32)
        elif ("a" <= s1[i] <='z') or ('0'<=s1[i]<="9"):
            nstr=nstr+s1[i]
    return nstr


def isanagrams(s1, s2):
    s1 = anagramfiltrations(s1)
    s2 = anagramfiltrations(s2)
    if len(s1) != len(s2):
        return False
    else:
        dict = {}
        # for i in range(len(s1)):
        #     if s1[i] in dict:
        #         dict[s1[i]] = dict[s1[i]] + 1
        #     else:
        #         dict[s1[i]] = 1

        #     if s2[i] in dict:
        #         dict[s2[i]] = dict[s2[i]] - 1
        #     else:
        #         dict[s2[i]] = -1


    # By using the in-built get method
        for i in range(len(s1)):
            dict[s1[i]] = dict.get(s1[i], 0) + 1
            dict[s1[i]] = dict.get(s1[i],0)-1

        print(dict)

        for key, val in dict.items():
            if val != 0:
                return False
        return True
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
res = isanagrams(s1, s2)
if res:
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")