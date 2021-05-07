import os
import sys
import math
from operator import itemgetter
"""
*************************************************************************************************************
Recebe um arquivo de ano e marca pacientes com condicoes consideradas de prioridade, tambem conta quantas dessas condicoes aquele
paciente possui, criando o campo apropriado
*************************************************************************************************************
"""
dirName = os.path.dirname(os.path.realpath(__file__)) 		
clear = lambda: os.system('cls')
if len(sys.argv) < 3:
	print("Argumentos insuficientes (Arquivo do ano, arquivo de saída)")		
	print("python fullGetPrioCondition.py h105Selected.csv h105PC.csv")
	exit(0)
filNameYear	 	 = sys.argv[1]										
filNameOutpt 	 = sys.argv[2]	

yearFile		 = open(dirName+"/1-Selected/"+filNameYear, "r", encoding="utf8")	
outputFile 		 = open(dirName+"/2-Condition/"+filNameOutpt, "w", encoding="utf8")								

yearHdr			 = yearFile.readline()
outputFile.write(yearHdr.strip() + ",PCFLAG,PCCOUNT\n")
yearHdr = yearHdr.split(",")

prioStrings = ["hibpdx", "chddx", "angidx", "midx", "ohrtdx", "strkdx", "asthdx", "emphdx", "cancerdx", "diabdx", "arthdx", "choldx"]
prioIndxs   = []
for el in prioStrings:
	i = 0
	found = 0
	for hdr in yearHdr:
		if el in hdr.strip().lower():
			prioIndxs.append(i)
			if found == 1:
				print("Indice repetido para " + el) 
			found = 1
		i+=1
for line in yearFile:
	pc 			= 2 #1 = sim, 2 = nao
	pccount 	= 0
	lineSpl 	= line.split(",")
	for el in prioIndxs:
		if int(lineSpl[el]) == 1:
			pccount+=1
	if pccount > 0:
		pc = 1
	outputFile.write(line.strip() + "," + str(pc) + "," + str(pccount) + "\n")

yearFile.close()
outputFile.close()

