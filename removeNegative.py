import os
import sys
import math
from operator import itemgetter
"""
*************************************************************************************************************
Muda a notacao de respostas invalidas do meps, trocando todos os valores nas variaveis aplicaveis para -1 
*************************************************************************************************************
"""
dirName = os.path.dirname(os.path.realpath(__file__)) 		
clear = lambda: os.system('cls')
if len(sys.argv) < 3:
	print("Argumentos insuficientes (Arquivo do ano, arquivo de saída)")		
	print("python fullRemoveNegative.py h105Vars.csv h105Final.csv")
	exit(0)

filNameYear		 = sys.argv[1]											
filNameOutput	 = sys.argv[2]	
yearFile		 = open(dirName+"/5-Vars/"+filNameYear, "r", encoding="utf8")	
outputFile 		 = open(dirName+"/6-Final/"+filNameOutput, "w", encoding="utf8")								
hdr = yearFile.readline()
outputFile.write(hdr)
hdr = hdr.split(",")
changed=0
varsList = ["DUPERSID","PANEL","CHOLDX53","CHDDX53","CHECK53","ARTHDX53","DIABDX53","ASTHDX53","EMPHDX53","STRKDX53","OHRTDX53","MIDX53","ANGIDX53","HIBPDX53","RXTOT","IPDIS","OBTOTV","OPTOTV","ERTOT","DENTCK53","STOOL53","BOWEL53","EXRCIS53","ASPRIN53","NOFAT53","CHOLCK53","BPCHEK53","ANYLIM","REGION","AGE","SEX","RACEX","MARRY","HIDEG","POVCAT","RTHLTH31","RTHLTH42","RTHLTH53","MNHLTH31","MNHLTH42","MNHLTH53","BMINDX53","TOTEXP","CANCERDX","TOTEXPY2","PCFLAG","PCCOUNT","HIGHCOST"]
indxsToLook = []
for elem in varsList:
	i=0
	for el in hdr:
		if elem.strip() in  el.strip():
			indxsToLook.append(i)
		i+=1
for line in yearFile:
	lineSpl = line.split(",")
	for indx in indxsToLook:
		try:
			if int(lineSpl[indx]) < 0:
				lineSpl[indx] = -1
				changed+=1
		except:
			if float(lineSpl[indx]) < 0.0:
				lineSpl[indx] = -1.0
				changed+=1
	strWrite = ""
	for el in lineSpl:
		strWrite = strWrite + str(el).strip() + ","
	strWrite = strWrite[:-1]
	strWrite = strWrite + "\n"
	outputFile.write(strWrite)
print("Changed: " + str(changed))
yearFile.close()
outputFile.close()


"""	for i in range(len(hdr)):
		try:
			if int(lineSpl[i]) < 0:
				lineSpl[i] = -1
				changed+=1
		except:
			if float(lineSpl[i]) < 0.0:
				lineSpl[i] = -1.0
				changed+=1
	strWrite = ""
	for el in lineSpl:
		strWrite = strWrite + str(el).strip() + ","
	strWrite = strWrite[:-1]
	strWrite = strWrite + "\n"
"""