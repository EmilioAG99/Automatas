from itertools import combinations 
file=open('automata.txt',"r")
lines = file.readline()
file.close()
substring = lines[1:len(lines)-1]
print(substring)
contcomas=0
contador=0
conaux=1
transicion = []
for letras in range(0, len(lines)): 
    contador+=1
    if lines[letras]== ",":
        contcomas+=1
    if contcomas==3:
        contcomas = 0
        transicion.append(lines[conaux :contador-1])
        contaux = contador+1

transicion.append(lines[conaux :len(lines)-1])
con=0      
for i in transicion:
    print(transicion[con])
    print("\n")
    con+=1
for i in range(0,5):
    comb = combinations(["p", "q", "r","s"], i) 
    for j in list(comb): 
       print(j)