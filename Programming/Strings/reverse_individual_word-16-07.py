#write a  program to reverse each indivicual word in a given string without reversing the order of the words

def reverse_word_sen(s1):
    s1=s1+" "     #Extra spacing for placing the last word in the senctence
    i=0
    nword=""   
    nsen=""
    while i<len(s1):
        if s1[i]!=" ":
            nword=s1[i]+nword
        elif nword!="":
            if nsen=="":
                nsen=nsen+nword
                nword=""
            else:
                nsen=nsen+" "+nword
                nword=""
        i+=1
       
    return nsen

def reverse_sentence(s1):
    s1=s1+" "
    i=0
    nword=""
    nsen=""
    while i<len(s1):
        if s1[i]!=" ":
            nword=nword+s1[i]
        elif nword!="":
            if nsen=="":
                nsen=nword+nsen
                nword=""
            else:
                nsen=nword+" "+nsen
                nword=""
        i+=1
    return nsen

s1=input("Enter the string")
res=reverse_word_sen(s1)
res1=reverse_sentence(s1)
print(f"Original sentance is {s1} ")
print(f"The reversed string is {res}")
print(f"The reverse sentence is {res1}")

#write a program to reverse the


