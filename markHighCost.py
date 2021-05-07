import os
import sys
import math
from operator import itemgetter
 
"""
*************************************************************************************************************
* Recebe como parâmetros um arquivo csv e um numero inteiro n
* Cria, para cada linha do arquivo de entrada uma variável HIGHCOST associada a linha atual, que terá valor 1, caso o valor
* de custo anual encontrado nessa linha esteja entre os maiores n% dos casos e 0 em caso contrário 
*************************************************************************************************************
"""

dirName = os.path.dirname(os.path.realpath(__file__)) 		#Diretorio atual
if len(sys.argv) < 5:
	print("Argumentos insuficientes (arquivo de entrada, porcentagem a ser considerada, nome do arquivo de saída, nome do campo representando as despesas)")		
	print("python fullMarkHighCost.py h121Expy2.csv 5 h121Marked.csv totexp0\n\t*(Para custo do primeiro ano usar totexpy0 até o ano de 2009, correspondente ao arquivo h129, para os anos subsequentes usar totexpy1.)\n\t*(Para custo do segundo ano usar sempre totexpy2)") #totexpy0 para o primeiro ano até 2009, totexpy1 de 2010 pra frente, totexpy2 para o segundo
	exit(0)


filNameInput = sys.argv[1]
percen = sys.argv[2]
filNameOutpt = sys.argv[3]
expTarget = sys.argv[4]

inputFile =  open(dirName+"/3-Expy2/"+filNameInput, "r", encoding="utf8")
outputFile = open(dirName+"/4-1-HighcostY2/"+filNameOutpt, "w", encoding="utf8")

hdrInput = inputFile.readline()
outputFile.write(hdrInput.strip() + ",HIGHCOST\n")

i = 0 
indxTarget = -1
hdrInput = hdrInput.split(",")
for el in hdrInput:
	if expTarget.lower() in el.lower():
		if indxTarget != -1:
			print("Indice repetido para " + expTarget)
			exit(0)
		else:
			indxTarget = i
	i+=1
if indxTarget == -1:
	print("Indice nao encontrado para " + expTarget)
	exit(0)

fileSize = 0
for line in inputFile:
	fileSize+=1

totalHighcost = fileSize * (int(percen)/100)
inputFile =  open(dirName+"/3-Expy2/"+filNameInput, "r", encoding="utf8")
hdrInput = inputFile.readline().split(",")
costRecord = []
i=0
for line in inputFile:
	lineSpl = line.split(",")
	if len(costRecord) <= totalHighcost:
		costRecord.append(tuple((i, int(lineSpl[indxTarget]))))
	else:
		costRecord.sort(key=itemgetter(1))
		if costRecord[0][1] < int(lineSpl[indxTarget]):
			costRecord[0] = tuple((i,int(lineSpl[indxTarget])))
	i+=1

costRecord.sort(key=itemgetter(0))

inputFile =  open(dirName+"/3-Expy2/"+filNameInput, "r", encoding="utf8")
hdrInput = inputFile.readline().split(",")
i = 0
for line in inputFile:
	if len(costRecord) > 0 and costRecord[0][0] == i:
		outputFile.write(line.strip() + ",1\n")
		j = costRecord.pop(0)
	else:
		outputFile.write(line.strip() + ",0\n")
	i+=1

inputFile.close()
outputFile.close()