#removi totexp e totexpy2 do arquivo, já que highcost ja esta marcado, mudar no arquivo que marca highcost
import os
import sys
import math
from operator import itemgetter
"""
*************************************************************************************************************
Seleciona os campos que serao incluidos no dataset final, listados no arquivo vars, passado como parametro
*************************************************************************************************************
"""
dirName = os.path.dirname(os.path.realpath(__file__)) 		
clear = lambda: os.system('cls')
if len(sys.argv) < 4:
	print("Argumentos insuficientes (Arquivo do ano, arquivo com as variaveis a serem extraídas, arquivo de saída)")		
	print("python fullSelectFields.py h105Final.csv vars0X.csv h105Input.csv")
	exit(0)

filNameYear		 = sys.argv[1]											
filNameVars		 = sys.argv[2]	
filNameOutput	 = sys.argv[3]	
yearFile		 = open(dirName+"/6-Final/"+filNameYear, "r", encoding="utf8")	
variableFile	 = open(dirName+"/"+filNameVars, "r", encoding="utf8")	
outputFile 		 = open(dirName+"/7-Input/"+filNameOutput, "w", encoding="utf8")								

yHdrOr 	= yearFile.readline()
yHdr 	= yHdrOr.split(",")

varsList = []
varsIndx = []
for line in variableFile:
	for el in line.split(","):
		if "age" not in el.lower().strip() and "sex" not in el.lower().strip() and "mcs" not in el.lower().strip():
			varsList.append(el.strip().lower())

for element in varsList:
	i = 0
	found = 0 
	for el in yHdr:
		if element.lower().strip() in el.lower().strip():
			if found == 0:
				varsIndx.append(i)
				found=1
			else:
				print("Índice repetido para " + element +" ("+el+", indice "+ str(i)+")" )
				exit(0)
		i+=1
	if found == 0:
		print("Índice não encontrado para " + element)
varsList.append("AGE53")
varsList.append("SEX")
varsList.append("MCS")
i = 0
found = 0
for el in yHdr:
	if "age53x" in el.lower().strip() and len(el) == 6:
		if found == 0:
			varsIndx.append(i)
			found = 1
		else:
			print("Indice repetido para age53")
			exit(0)
	i+=1
if found == 0:
	print("Índice nao encontrado para age53")
	exit(0)

i = 0
found = 0
for el in yHdr:
	if "sex" in el.lower().strip() and len(el) == 3:
		if found == 0:
			varsIndx.append(i)
			found = 1
		else:
			print("Indice repetido para sex")
			exit(0)
	i+=1
if found == 0:
	print("Índice nao encontrado para sex")
	exit(0)

i = 0
found = 0
for el in yHdr:
	if "mcs42" in el.lower().strip() and len(el) == 5:
		if found == 0:
			varsIndx.append(i)
			found = 1
		else:
			print("Indice repetido para mcs")
			exit(0)
	i+=1
if found == 0:
	print("Índice nao encontrado para mcs")
	exit(0)

wrStr = ""
for el in varsList:
	wrStr += el.upper() + ","
wrStr = wrStr[:-1] + "\n"
outputFile.write(wrStr)
for line in yearFile:
	lineSpl = line.split(",")
	writeStr = ""
	for el in varsIndx:
		writeStr += lineSpl[el].strip() + ","
	writeStr = writeStr[:-1] + "\n"
	outputFile.write(writeStr)
yearFile.close()
outputFile.close()
variableFile.close()
"""
Attributes 
	Demographic
		Age31X
		Sex	
		Racex
		Educyr
		Hideg
		Region
		Marry
		TTLP	Total income
		PovCat
	Health Status
		PCS 	SAQ:PHY Component Summary
		MCS 	SAQ:MNT Component Summary
		RTHLTH
		MNHLTH
		IADLHP IADL Screener
		ADLHLP ADL Screener
		WLKLIM Walking limitation
			LFTDIF Lifting 10 pounds
			STPDIF 	Walking 10 steps
			WLKDIF Walking 3 blocks
			MILDIF Walking a Mile
			STNDIF Standing 20 mins
		ANYLIM Any limitation
		AIDHLP Used assistive devices
		ACTLIIM An limitations
		COGLIM Cognitive limitations
		BMINDX Body mass index
	Preventive Care Attributes
		Check
		BPCHEK
			BPMONT 	 
		CHOLCK
		NOFAT
		EXRCIS
		ASPRIN
			PSA
		BOWEL
		STOOL
			MAMOGR
			BRSTEX
			PAPSMR
			HYSTER
		DENTCK
		LSTETH	LOST ALL UPPER AND LOWER TEETH
	Priority Conditions
		HIBPDX
		CHDDX
		ANGIDX
		MIDX
		OHRTDX
		STRKDX
		ASTHDX
		EMPHDX
		CANCERDX
		DIABDX
		ARTHDX
		CHOLDX
		PC
		PCCOUNT
	Visits Counts Attributes
		OBTOTV	
		OBDRV 	OFFICE BASED PHYSICIAN VISITS
		OBOTHV	OFFICE BASED NON PHYS VISITS
		OPTOTV
		OPDRV
		OPOTHV
		ERTOT
		IPDIS
		IPNGTD 	NIGHT IN HOSP FOR DISCHARGES
		RXTOT

SELECTED FOR THE FINAL DATASET
	Demographics 	: AGE, SEX, RACE, HIDEG, REGION, MARRY, and POVCAT
	Health Status  RTHLTH, MNHLTH, ANYLIM, and BMINDX
	Preventive Care CHECK, BPCHEK, CHOLCK, NOFAT, EXRCIS, ASPRIN, BOWEL, STOOL, and DENTCK.
	Priority Conditions HIBPDX, CHDDX, ANGIDX, MIDX, OHRTDX, STRKDX, ASTHDX, EMPHDX, CANCERDX, DIABDX, ARTHDX, CHOLDX, PC, and PCCOUNT.
	Visit Counts OBTOT, OPTOT, ERTOT, IPDIS, and RXTOT (

Missing
	Demographic
		Educyr #igual ao que foi substituido nos arquivos futuros?
		TTLP	Total income
	Health Status
		PCS 	SAQ:PHY Component Summary
		MCS 	SAQ:MNT Component Summary
		IADLHP IADL Screener
		ADLHLP ADL Screener
		WLKLIM Walking limitation
			LFTDIF Lifting 10 pounds
			STPDIF 	Walking 10 steps
			WLKDIF Walking 3 blocks
			MILDIF Walking a Mile
			STNDIF Standing 20 mins
		AIDHLP Used assistive devices
		ACTLIIM An limitations
		COGLIM Cognitive limitations
	Preventive Care Attributes
			BPMONT 	 
			PSA
			MAMOGR
			BRSTEX
			PAPSMR
			HYSTER
		LSTETH	LOST ALL UPPER AND LOWER TEETH
	Visits Counts Attributes
		OBDRV 	OFFICE BASED PHYSICIAN VISITS
		OBOTHV	OFFICE BASED NON PHYS VISITS
		OPDRV
		OPOTHV
		IPNGTD 	NIGHT IN HOSP FOR DISCHARGES
i
"""