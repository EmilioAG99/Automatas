from itertools import combinations
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
print("QD= {",end=" ")
for i in range(0,len(states)+1):
    comb = combinations(states, i) 
    for j in list(comb):
       if i==len(states):  
        print(j, end=" ")
       else:
           print(j, end=",")
print("}\n")