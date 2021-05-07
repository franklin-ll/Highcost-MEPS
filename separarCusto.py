import os
import sys
import math
from operator import itemgetter
"""
*************************************************************************************************************
Separa o dataset completo em dois arquivos separados, um contendo apenas pacientes de alto custo
e o outro contendo os demais
*************************************************************************************************************
"""
dirName = os.path.dirname(os.path.realpath(__file__)) 		
clear = lambda: os.system('cls')
if len(sys.argv) < 4:
	print("Argumentos insuficientes (Arquivo de entrada, arquivo de alto cust, arquivo de baixo custo)")		
	print("python fullSepararCusto.py outputCats.csv outputCatsHC.csv outputCatsLC.csv")
	exit(0)

filNameInput	 = sys.argv[1]											
filNameOutputHC	 = sys.argv[2]	
filNameOutputLC	 = sys.argv[3]	
inputFile		 = open(dirName+"/7-Input/"+filNameInput, "r", encoding="utf8")	
outputFileHC	 = open(dirName+"/7-Input/"+filNameOutputHC, "w", encoding="utf8")								
outputFileLC	 = open(dirName+"/7-Input/"+filNameOutputLC, "w", encoding="utf8")								

hdr = inputFile.readline().split(",")
indxDupersid = -1
indxPanel = -1
indxHighcost = -1
i=0
for el in hdr:
	if "DUPERSID" in el:
		indxDupersid = i
	elif "PANEL" in el:
		indxPanel = i
	elif "HIGHCOST" in el:
		indxHighcost = i
	i+=1
i = 0
strWr = ""
for el in hdr:
	if i != indxDupersid and i != indxPanel:
		strWr = strWr + el.strip() + ","
	i+=1
strWr = strWr[:-1] + "\n"
outputFileHC.write(strWr)
outputFileLC.write(strWr)

for line in inputFile:
	lineSpl = line.split(",")
	i = 0
	strWr = ""
	for el in lineSpl:
		if i != indxDupersid and i != indxPanel:
			strWr = strWr + el.strip() + ","
		i+=1
	strWr = strWr[:-1] + "\n"
	if int(lineSpl[indxHighcost]) == 1:
		outputFileHC.write(strWr)
	else:
		outputFileLC.write(strWr)

inputFile.close()
outputFileHC.close()
outputFileLC.close()