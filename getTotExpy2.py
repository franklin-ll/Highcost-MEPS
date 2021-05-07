import os
import sys
import math
from operator import itemgetter
"""
*************************************************************************************************************
* Recebe dois arquivos, um de um ano do meps e outro um arquivo longitudinal correspondente ao painel a ser
* considerado no arquivo inicial e recupera, para cada paciente, a despesa total do segundo ano (TOTEXPY2)
*************************************************************************************************************
"""
dirName = os.path.dirname(os.path.realpath(__file__)) 		
clear = lambda: os.system('cls')
if len(sys.argv) < 4:
	print("Argumentos insuficientes (Arquivo do ano, arquivo longitudinal, arquivo de saída)")		
	print("python getTotexpy2.py h105PC.csv h114.csv h105Expy2.csv")
	exit(0)


filNameYear		 = sys.argv[1]										
filNameLongit	 = sys.argv[2]										
filNameOutpt	 = sys.argv[3]

yearFile		 = open(dirName+"/2-Condition/"+filNameYear, "r", encoding="utf8")	
longitFile		 = open(dirName+"/"+filNameLongit, "r", encoding="utf8")	
outputFile 		 = open(dirName+"/3-Expy2/"+filNameOutpt, "w", encoding="utf8")

yearHdr = yearFile.readline()
outputFile.write(yearHdr.strip() + ",TOTEXPY2\n")

fileLen = 0
for l in yearFile:
	fileLen+=1


yearFile		   = open(dirName+"/2-Condition/"+filNameYear, "r", encoding="utf8")	
yearHdr 		   = yearFile.readline()

longitHdr 		   = longitFile.readline().split(",")
yearHdr			   = yearHdr.split(",")
panelIndxYear 	   = -1
dupersidIndxYear   = -1
panelIndxLongit    = -1
totexpy2IndxLongit = -1
dupersidIndxLongit = -1
i = 0

for el in yearHdr:
	if "dupersid" in el.lower().strip():
		if dupersidIndxYear != -1:
			print("Indice repetido (dupersid - year)")
			exit(0)
		dupersidIndxYear = i
	if "panel" in el.lower().strip():
		if panelIndxYear != -1:
			print("Indice repetido (panel- year)")
			exit(0)
		panelIndxYear = i
	i+=1

print("Panel indx year: " + str(panelIndxYear) + "\nDupersid indx year: " + str(dupersidIndxYear))

i = 0

for el in longitHdr:
	if "dupersid" in el.lower().strip():
		if dupersidIndxLongit != -1:
			print("Indice repetido (dupersid - longit)")
			exit(0)
		dupersidIndxLongit = i
	if "panel" in el.lower().strip():
		if panelIndxLongit != -1:
			print("Indice repetido (panel- longit)")
			exit(0)
		panelIndxLongit = i
	if "totexpy2" in el.lower().strip():
		if totexpy2IndxLongit != -1:
			print("Indice repetido (totexpy2 - longit)")
			exit(0)
		totexpy2IndxLongit = i
	i+=1

print("Panel indx longit: " + str(panelIndxLongit) + "\nDupersid indx longit: " + str(dupersidIndxLongit))
i=0
missing = 0
for line in yearFile:
	print((i/fileLen)*100)
	i+=1
	lineSpl = line.split(",")
	target = lineSpl[panelIndxYear].strip() + lineSpl[dupersidIndxYear] 
	found = 0
	longitFile		 = open(dirName+"/"+filNameLongit, "r", encoding="utf8")	
	longitHdr 		   = longitFile.readline().split(",")
	for rec in longitFile:
		recSpl = rec.split(",")
		currTarget = recSpl[panelIndxLongit] + recSpl[dupersidIndxLongit]
		#Nao testado em paines acima de 22, aparentemente dupersid no arquivo longit do painel 22 ja vem com panel junto
		if int(recSpl[panelIndxLongit]) == 22:
			currTarget = recSpl[dupersidIndxLongit]
		if currTarget == target:
			outputFile.write(line.strip() + "," + recSpl[totexpy2IndxLongit].strip() + "\n")
			found = 1
		if found:
			break
	if not found:
		missing+=1
print(str(missing) + " missing")

yearFile.close()	
longitFile.close()	
outputFile.close()
