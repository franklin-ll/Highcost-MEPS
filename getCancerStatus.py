import os
import sys
import math
from operator import itemgetter
"""
*************************************************************************************************************
* Recebe um arquivo de ano do meps e um arquivo com condições médicas para aquele ano, cria um terceiro 
* arquivo, anotando os pacientes que foram diagnosticados com cancer
*************************************************************************************************************
"""
dirName = os.path.dirname(os.path.realpath(__file__)) 		
clear = lambda: os.system('cls')
if len(sys.argv) < 4:
	print("Argumentos insuficientes (Arquivo do ano, arquivo de condicoes, arquivo de saída)")		
	print("python fullGetCancerStatus.py h105Selected.csv h104Selected.csv h105Status.csv")
	exit(0)

filNameYear		 = sys.argv[1]										
filNameCondition = sys.argv[2]										
filNameOutpt	 = sys.argv[3]

yearFile		 = open(dirName+"/1-Selected/"+filNameYear, "r", encoding="utf8")	
conditionFile	 = open(dirName+"/"+filNameCondition, "r", encoding="utf8")	
conditionHdr 	 = conditionFile.readline().split(",") 
yearHdr			 = yearFile.readline()
outputFile 		 = open(dirName+"/1-Selected/"+filNameOutpt, "w", encoding="utf8")								
yearLen = 0
for line in yearFile:
	yearLen+=1
yearFile		 = open(dirName+"/1-Selected/"+filNameYear, "r", encoding="utf8")	
yearHdr			 = yearFile.readline()

outputFile.write(yearHdr.strip() + ",CANCERDX\n")
yearHdr = yearHdr.split(",")

fileLen			 	  = 0
yearPanelIndx 	 	  = -1
yearDupersidIndx 	  = -1
conditionPanelIndx 	  = -1
conditionDupersidIndx = -1
conditionCccodexIndx  = -1
i = 0
for element in yearHdr:
	if "panel" in element.strip().lower():
		if yearPanelIndx != -1:
			print("Indice repetido year panel")
		yearPanelIndx = i
	if "dupersid" in element.strip().lower():
		if yearDupersidIndx != -1:
			print("Indice repetido year dupersid")
		yearDupersidIndx = i
	i+=1
if yearPanelIndx == -1 or yearDupersidIndx == -1:
	print("Indice nao encontrado (year)")
	exit(0)
i=0

for element in conditionHdr:
	if "panel" in element.strip().lower():
		if conditionPanelIndx != -1:
			print("Indice repetido condition panel")
		conditionPanelIndx = i
	if "dupersid" in element.strip().lower():
		if conditionDupersidIndx != -1:
			print("Indice repetido condition dupersid")
		conditionDupersidIndx = i
	if "cccodex" in element.strip().lower():
		if conditionCccodexIndx != -1:
			print("Indice repetido condition cccodex")
		conditionCccodexIndx = i
	i+=1
if conditionPanelIndx == -1 or conditionDupersidIndx == -1:
	print("Indice nao encontrado (condition)")
	exit(0)
i=0

for line in yearFile:
	print((i/yearLen)*100)
	i+=1
	lineSpl = line.split(",")
	target = lineSpl[yearPanelIndx].strip() + lineSpl[yearDupersidIndx].strip() 
	conditionFile	 = open(dirName+"/"+filNameCondition, "r", encoding="utf8")	
	conditionHdr 	 = conditionFile.readline().split(",") 
	found = 0
	for el in conditionFile:
		elSpl = el.split(",")
		currTarget = elSpl[conditionPanelIndx].strip() + elSpl[conditionDupersidIndx].strip()
		if target == currTarget:
			if int(elSpl[conditionCccodexIndx]) > 10 and int(elSpl[conditionCccodexIndx]) < 46:
				found = 1
				outputFile.write(line.strip() + ",1\n")
		if found:
			break
	if not found:
		outputFile.write(line.strip() + ",2\n")
yearFile.close()
conditionFile.close()
outputFile.close()