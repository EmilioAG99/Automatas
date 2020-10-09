from itertools import combinations
from collections import OrderedDict
import re
file=open('automata.txt',"r")
lines = file.readline()
file.close()
regex=r"\(([a-z0-9,]*)\)"
delta=re.findall(regex,lines)
s=''
print("transitions rules NFA= ",delta)
#print(len(delta))
aux=delta[0][2]
print("q0= ",aux)
aux2=delta[0][0]
language=[]
states=[]
states.append(aux)
language.append(aux2)
for rule in delta:
    if rule[2]!=aux:
        aux=rule[2]
        states.append(aux)
    if (rule[0]!=aux2 and rule[0] not in language):
        aux2=rule[0]
        language.append(aux2)
for state in states:
    if (len(s)==0):
        s="{"+state
    else:
        s=s+","+state
s+="}"
print("States QN=",s)
lan=""

    
print("Language ",language)
statessize= len(states)


combinationList=[]
print("QD= {",end=" ")
for i in range(0,len(states)+1):
    comb = combinations(states, i) 
    for j in list(comb):
       combinationList.append(j)
       if i==len(states):  
        print(j, end=" ")
       else:
           print(j, end=",")
print("}\n")


#Transition table
tranList=[]
print("DFA")
empty0 = tuple(('Ø','0',"Ø"))
empty1 = tuple(('Ø','1',"Ø"))
tranList.append(empty0)
tranList.append(empty1)


for combin in range(1,pow(2,statessize)):
    c=""
    x=combinationList[combin]
    for len in language:
      aux2=len
      for var in x:
         for elem in delta:
             if(elem[0]==aux2 and elem[2]==var) :
                c= c + elem[4] + ""
            
      if(c==""):
        c="Ø"
      table = tuple((x,aux2,("".join(OrderedDict.fromkeys(c)))))
      tranList.append(table)
      c=""   
out=open('DFA.txt','w')  
out.write('{')
cont=0    
for transitions in tranList:
    document=str(transitions)
    document=document.replace("'","")
    document=document.replace(",)",")")
    print(document)
    out.write(document)
    cont+=1
    out.write(",")
out.write('}')
out.close()
 
