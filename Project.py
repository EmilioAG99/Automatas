from itertools import combinations
from collections import OrderedDict
import re
file=open('automata.txt',"r")
lines = file.readline()
file.close()
regex=r"\(([a-z0-9,]*)\)"
delta=re.findall(regex,lines)
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

print("States QN= ",states)
print("Language ",language)
statessize= len(states)
# substring = lines[1:len(lines)-1]
# print(substring)
# contcomas=0
# contador=0
# conaux=1
# transicion = []
# for letras in range(0, len(lines)): 
#     contador+=1
#     if lines[letras]== ",":
#         contcomas+=1
#     if contcomas==3:
#         contcomas = 0
#         transicion.append(lines[conaux :contador-1])
#         contaux = contador+1

# transicion.append(lines[conaux :len(lines)-1])
# con=0      
# for i in transicion:
#     print(transicion[con])
#     print("\n")
#     con+=1
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
#for sta in states:
#    aux=sta
#    c= ""
#    for len in language:
#     aux2=len
#    for elem in delta:
  #        if(elem[0]==aux2 and elem[2]==aux) :
  #           c= c + elem[4] + " "
 #     if(c==""):
  #        c="Ø"
  #    table = tuple((aux,aux2,c))
  #    tranList.append(table)
 #     c=""
#Transition for combinations
for combin in range(1,pow(2,statessize)):
    c=""
    x=combinationList[combin]
    for len in language:
      aux2=len
      for var in x:
         for elem in delta:
             if(elem[0]==aux2 and elem[2]==var) :
                c= c + elem[4] + " "
            
      if(c==""):
        c="Ø"
      table = tuple((x,aux2,("".join(OrderedDict.fromkeys(c)))))
      tranList.append(table)
      c=""   
      
for transitions in tranList:
    print(transitions)

 
