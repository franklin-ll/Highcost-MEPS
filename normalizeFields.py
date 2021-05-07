import os
import sys
import math
from operator import itemgetter
"""
*************************************************************************************************************
Normaliza os campos adicionados que nao estavam presentes no dataset orignial
*************************************************************************************************************
"""
dirName = os.path.dirname(os.path.realpath(__file__)) 		
clear = lambda: os.system('cls')
if len(sys.argv) < 3:
	print("Argumentos insuficientes (Arquivo de entrada, arquivo de saída)")		
	print("python fullNormalizeFields.py output.csv outputNormalized.csv")
	exit(0)

filNameInput	 = sys.argv[1]											
filNameOutput	 = sys.argv[2]	
inputFile		 = open(dirName+"/7-Input/"+filNameInput, "r", encoding="utf8")	
outputFile 		 = open(dirName+"/7-Input/"+filNameOutput, "w", encoding="utf8")								
#varNames 		 = ["TTLP","PCS","IADLHP","ADLHLP","WLKLIM","LFTDIF","STPDIF","WLKDIF","MILDIF","STNDIF","AIDHLP","ACTLIM","COGLIM","LSTETH","OBDRV","OBOTHV","OPDRV","OPOTHV","MCS"]
varNames 		 = ["TTLP","PCS","OBDRV","OBOTHV","OPDRV","OPOTHV","MCS"]

hdrInpt = inputFile.readline().split(",")
varIndxs = []
for el in varNames:
	found =0
	i=0
	for elInpt in hdrInpt:
#		print("if " + el + " in " + elInpt + " = " + str(el in elInpt))
		if el in elInpt:
			if found == 0:
				found = 1
				varIndxs.append(i)
			else:
				print("Indice repetido para " + el)
				exit(0)
		i+=1
	if found==0:
		print("Indice nao encontrado para " + el)
		exit(0)
#print(varIndxs)
minAll = []
maxAll = []

firstLine = inputFile.readline().split(",")
for element in varIndxs:
	minAll.append(float(firstLine[element]))
	maxAll.append(float(firstLine[element]))

for line in inputFile:
	lineSpl = line.split(",")
	i = 0
	for element in varIndxs:
		if float(lineSpl[element]) < float(minAll[i]):
			minAll[i] = float(lineSpl[element])
		if float(lineSpl[element]) > float(maxAll[i]):
			maxAll[i] = float(lineSpl[element])
		i+=1

inputFile	= open(dirName+"/7-Input/"+filNameInput, "r", encoding="utf8")	
hdr	= inputFile.readline()
outputFile.write(hdr)
numline=0
for line in inputFile:
	numline+=1
	lineSpl = line.split(",")
	i = 0
	for el in varIndxs:
		if len(lineSpl[el].split(".")) > 1:
			lineSpl[el] = round((float(lineSpl[el])-minAll[i])/(maxAll[i]-minAll[i]),2)
		else:
			lineSpl[el] = round((int(lineSpl[el])-minAll[i])/(maxAll[i]-minAll[i]),2)
		i+=1
	writeStr = ""
	for rec in lineSpl:
		writeStr = writeStr + str(rec).strip() + ","
	writeStr = writeStr[:-1]+"\n"
	outputFile.write(writeStr)

inputFile.close()
outputFile.close()
"""
		if isinstance(lineSpl[el],float):
			lineSpl[el] = (float(lineSpl[el])-float(minAll[i]))/(float(maxAll[i])-float(minAll[i]))
		elif isinstance(lineSpl[el],int):
			lineSpl[el] = (int(lineSpl[el])-int(minAll[i]))/(int(maxAll[i])-int(minAll[i]))
		elif isinstance(lineSpl[el], str):
			print("Strng")
		else:
			print("Erro de tipo na variável " + str(lineSpl[el]))
			exit(0)
"""