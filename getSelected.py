import os
import sys
import math
from operator import itemgetter
"""
******************************************************************************************************************
* Recebe um arquivo de ano do meps e cria um segundo arquivo contendo todas as linhas do primeiro arquivo que
* atendem as condições da linha 60 (idade > 17, perwtf > 0, painel selecionado por parametro e custo total >=0 )
******************************************************************************************************************
"""
dirName = os.path.dirname(os.path.realpath(__file__)) 		
clear = lambda: os.system('cls')
if len(sys.argv) < 4:
	print("Argumentos insuficientes (Arquivo de entrada, arquivo de saída, painel selecionado)")		
	print("python fullGetSelected.py h105.csv h105Selected.csv 11")
	exit(0)

filNameYear		 = sys.argv[1]										
filNameOutpt	 = sys.argv[2]
targetPanel 	 = sys.argv[3]

yearFile		 = open(dirName+"/"+filNameYear, "r", encoding="utf8")	
yearHdr			 = yearFile.readline()
outputFile 		 = open(dirName+"/1-Selected/"+filNameOutpt, "w", encoding="utf8")								
outputFile.write(yearHdr)
yearHdr = yearHdr.split(",")

yearPanelIndx 	 	  = -1
yearAgeIndx 	  = -1
yearTotexpIndx 	  = -1
yearPerwtIndx = -1
i = 0
for el in yearHdr:
	if "panel" in el.lower().strip():
		if yearPanelIndx != -1:
			print("Indice repetido para panel")
			exit(0)
		yearPanelIndx = i
	if "age0" in el.lower().strip() or "age1" in el.lower().strip():
		if yearAgeIndx != -1:
			print("Indice repetido para age")
			exit(0)
		yearAgeIndx = i
	if "totexp" in el.lower().strip():
		if yearTotexpIndx != -1:
			print("Indice repetido para totexp")
			exit(0)
		yearTotexpIndx = i
	if "perwt" in el.lower().strip():
		if yearPerwtIndx != -1:
			print("Indice repetido para perwt")
			exit(0)
		yearPerwtIndx = i
	i+=1	


numLines = 0
for line in yearFile:
	lineSpl = line.split(",")
	if (int(lineSpl[yearAgeIndx]) > 17) and (float(lineSpl[yearPerwtIndx])>0.0) and (float(lineSpl[yearTotexpIndx]) >= 0.0) and (int(lineSpl[yearPanelIndx]) == int(targetPanel)):
		outputFile.write(line)
		numLines+=1
print(numLines)
yearFile.close()
outputFile.close()