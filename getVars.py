import os
import sys
import math
from operator import itemgetter
"""
************************************************************************************************************************
Trata os campos que serao convertidos de valores inteiros ou categoricos para valores que representam um intervalo ou agrupamento
de categorias, por exemplo 18-49 anos para idade será convertido para o valor 1, 49-65 para 2, etc
************************************************************************************************************************
"""
dirName = os.path.dirname(os.path.realpath(__file__)) 		
clear = lambda: os.system('cls')
if len(sys.argv) < 3:
	print("Argumentos insuficientes (Arquivo do ano, arquivo de saída)")		
	print("python fullGetVars.py h105Marked.csv h105Vars.csv")
	exit(0)


filNameYear		 = sys.argv[1]										
filNameOutput	 = sys.argv[2]	
yearFile		 = open(dirName+"/4-1-HighcostY2/"+filNameYear, "r", encoding="utf8")	
outputFile 		 = open(dirName+"/5-Vars/"+filNameOutput, "w", encoding="utf8")								
hdr = yearFile.readline().split(",")

ageIndx = -1
raceIndx = -1
hidegIndx = -1
marryIndx = -1
povcatIndx = -1
bmindxIndx = -1
pccountIndx = -1
checkIndx = -1
bpchekIndx = -1
cholckIndx = -1
dentckIndx = -1
obtotIndx = -1
rxtotIndx = -1
optotIndx = -1
ertotIndx = -1
ipdisIndx = -1

##
sgmtstIndx  = -1
clntstIndx  = -1 
bststIndx   = -1
eduyrdgIndx = -1
##
altHideg = 0

i = 0
count = 0
for el in hdr:
	if "age53" in el.lower().strip() and "chl" not in el.lower().strip():
		if ageIndx != -1:
			print("Indice repetido para age")
			count-=1
		ageIndx = i
		count+=1
	if "racex" in el.lower().strip() or "racev1x" in el.lower().strip():
		if raceIndx != -1:
			count-=1
			print("Indice repetido para race")
		count+=1
		raceIndx = i
	if "hideg" in el.lower().strip():
		if hidegIndx != -1:
			count-=1
			print("Indice repetido para hideg")
		count+=1
		hidegIndx = i
	if ("eduyrdg" in el.lower().strip()) and ("171" in filNameYear or "163" in filNameYear):
		if hidegIndx != -1:
			count-=1
			print("Indice repetido para hideg")
		altHideg = 1
		count+=1
		hidegIndx = i		

	if "marry53" in el.lower().strip():
		if marryIndx != -1:
			count-=1
			print("Indice repetido para marry")
		count+=1
		marryIndx = i
	if "povcat" in el.lower().strip():
		if povcatIndx != -1:
			count-=1
			print("Indice repetido para povcat")
		count+=1
		povcatIndx = i
	if "bmindx" in el.lower().strip():
		if bmindxIndx != -1:
			count-=1
			print("Indice repetido para bmindx")
		count+=1
		bmindxIndx = i
	if "adbmi" in el.lower().strip():
		print("ADBMIIII")
		exit(0)
	if "pccount" in el.lower().strip():
		if pccountIndx != -1:
			count-=1
			print("Indice repetido para pccount")
		count+=1
		pccountIndx = i
	if "check" in el.lower().strip():
		if checkIndx != -1:
			count-=1
			print("Indice repetido para check")
		count+=1
		checkIndx = i
	if "bpchek" in el.lower().strip():
		if bpchekIndx != -1:
			count-=1
			print("Indice repetido para bpchek")
		count+=1
		bpchekIndx = i
	if "cholck" in el.lower().strip():
		if cholckIndx != -1:
			count-=1
			print("Indice repetido para cholck")
		count+=1
		cholckIndx = i
	if "dentck" in el.lower().strip():
		if dentckIndx != -1:
			count-=1
			print("Indice repetido para dentck")
		count+=1
		dentckIndx = i
	if "obtotv" in el.lower().strip():
		if obtotIndx != -1:
			count-=1
			print("Indice repetido para obtot")
		count+=1
		obtotIndx = i
	if "rxtot" in el.lower().strip():
		if rxtotIndx != -1:
			count-=1
			print("Indice repetido para rxtot")
		count+=1
		rxtotIndx = i
	if "optotv" in el.lower().strip():
		if optotIndx != -1:
			count-=1
			print("Indice repetido para optot")
		count+=1
		optotIndx = i
	if "ertotv" in el.lower().strip() or "ertot0" in el.lower().strip() or "ertot1" in el.lower().strip():
		if ertotIndx != -1:
			count-=1
			print("Indice repetido para ertot")
		count+=1
		ertotIndx = i
	if "ipdis" in el.lower().strip():
		if ipdisIndx != -1:
			count-=1
			print("Indice repetido para ipdis")
		ipdisIndx = i
		count+=1
	if "sgmtst" in el.lower().strip():
		if sgmtstIndx != -1:
			count-=1
			print("Indice repetido para sgmtst")
		sgmtstIndx = i
		count+=1
	if "clntst" in el.lower().strip():
		if clntstIndx != -1:
			count-=1
			print("Indice repetido para clntst")
		clntstIndx = i
		count+=1
	if "bstst" in el.lower().strip():
		if bststIndx != -1:
			count-=1
			print("Indice repetido para bstst")
		bststIndx = i
		count+=1
	i+=1


if bststIndx != -1:
	hdr[bststIndx] = "STOOL53"
if clntstIndx != -1:
	hdr[clntstIndx] = "BOWEL53"
if sgmtstIndx != -1:
	del hdr[sgmtstIndx]
strWrite = ""
for el in hdr:
	strWrite += str(el).strip() + ","
strWrite = strWrite[:-1]
strWrite += "\n"
outputFile.write(strWrite)

if ageIndx == -1:
	print("Sem indice para age53")
	exit(0)
if raceIndx == -1:
	print("Sem indice para racex")
	exit(0)
if hidegIndx == -1:
	print("Sem indice para hideg")
	exit(0)
if marryIndx == -1:
	print("Sem indice para marry53")
	exit(0)
if povcatIndx == -1:
	print("Sem indice para povcat")
	exit(0)
if bmindxIndx == -1:
	print("Sem indice para bmindx")
	exit(0)
if pccountIndx == -1:
	print("Sem indice para pccount")
	exit(0)
if checkIndx == -1:
	print("Sem indice para check")
	exit(0)
if bpchekIndx == -1:
	print("Sem indice para bpchek")
	exit(0)
if cholckIndx == -1:
	print("Sem indice para cholck")
	exit(0)
if dentckIndx == -1:
	print("Sem indice para dentck")
	exit(0)
if obtotIndx == -1:
	print("Sem indice para obtotv")
	exit(0)
if rxtotIndx == -1:
	print("Sem indice para rxtot")
	exit(0)
if optotIndx == -1:
	print("Sem indice para optotv")
	exit(0)
if ertotIndx == -1:
	print("Sem indice para ertotv")
	exit(0)
if ipdisIndx == -1:
	print("Sem indice para ipdis")
	exit(0)

for line in yearFile:
	lineSplit = line.split(",")
	if int(lineSplit[ageIndx]) <= 49:
		lineSplit[ageIndx] = 1
	elif int(lineSplit[ageIndx]) <= 65:
		lineSplit[ageIndx] = 2
	elif int(lineSplit[ageIndx]) > 65:
		lineSplit[ageIndx] = 3
	if int(lineSplit[raceIndx]) > 2:
		lineSplit[raceIndx] = 3

	if altHideg == 0:
		if int(lineSplit[hidegIndx]) >= 4 and int(lineSplit[hidegIndx]) <= 6:
			lineSplit[hidegIndx] = 1
		else:
			lineSplit[hidegIndx] = 2
	else:
		if int(lineSplit[hidegIndx]) == 8 or int(lineSplit[hidegIndx]) == 9:
			lineSplit[hidegIndx] = 1
		else:
			lineSplit[hidegIndx] = 2

	if int(lineSplit[marryIndx]) >= 2 and int(lineSplit[marryIndx]) <= 4:
		lineSplit[marryIndx] = 2
	elif int(lineSplit[marryIndx]) > 4:
		lineSplit[marryIndx] = 0

	if int(lineSplit[povcatIndx]) == 1 or int(lineSplit[povcatIndx]) == 2:
		lineSplit[povcatIndx] = 1
	elif int(lineSplit[povcatIndx]) == 3 or int(lineSplit[povcatIndx]) == 4:
		lineSplit[povcatIndx] = 2
	else:
		lineSplit[povcatIndx] = 3

	if float(lineSplit[bmindxIndx]) <= 18.5:
		lineSplit[bmindxIndx] = 1
	elif float(lineSplit[bmindxIndx]) < 25:
		lineSplit[bmindxIndx] = 2
	elif float(lineSplit[bmindxIndx]) < 30:
		lineSplit[bmindxIndx] = 3
	elif float(lineSplit[bmindxIndx]) >=30:
		lineSplit[bmindxIndx] = 4

	if int(lineSplit[pccountIndx]) > 3:
		lineSplit[pccountIndx] = 4

	if int(lineSplit[checkIndx]) <= 1:
		lineSplit[checkIndx] = 1
	elif int(lineSplit[checkIndx]) == 6:
		lineSplit[checkIndx] = 0
	else:
		lineSplit[checkIndx] = 2

	if int(lineSplit[bpchekIndx]) <= 1:
		lineSplit[bpchekIndx] = 1
	elif int(lineSplit[bpchekIndx]) == 6:
		lineSplit[bpchekIndx] = 0
	else:
		lineSplit[bpchekIndx] = 2

	if int(lineSplit[cholckIndx]) <= 1:
		lineSplit[cholckIndx] = 1
	elif int(lineSplit[cholckIndx]) == 6:
		lineSplit[cholckIndx] = 0
	else:
		lineSplit[cholckIndx] = 2

	if int(lineSplit[dentckIndx]) == 2 or int(lineSplit[dentckIndx]) == 3:
		lineSplit[dentckIndx] = 2
	elif int(lineSplit[dentckIndx]) == 4:
		lineSplit[dentckIndx] = 0

	if int(lineSplit[obtotIndx]) <= 4:
		lineSplit[obtotIndx] = 0
	else:
		lineSplit[obtotIndx] = 1

	if int(lineSplit[rxtotIndx]) <= 11:
		lineSplit[rxtotIndx] = 0
	else:
		lineSplit[rxtotIndx] = 1

	if int(lineSplit[optotIndx]) >= 1:
		lineSplit[optotIndx] = 1

	if int(lineSplit[ertotIndx]) >= 1:
		lineSplit[ertotIndx] = 1

	if int(lineSplit[ipdisIndx]) >= 1:
		lineSplit[ipdisIndx] = 1

	if (sgmtstIndx != -1 and clntstIndx == -1) or (sgmtstIndx == -1 and clntstIndx != -1):
		print("Indice de clntst ou sgmtst nao encontrado")
		exit(0)
	elif sgmtstIndx != -1 and clntstIndx != -1:
		if lineSplit[sgmtstIndx] != 7 and lineSplit[clntstIndx] != 7:
			lineSplit[clntstIndx] = 1
		else:
			lineSplit[clntstIndx] = 2

	if bststIndx != -1:
		if lineSplit[bststIndx] != 7:
			lineSplit[bststIndx] = 1
		else:
			lineSplit[bststIndx] = 2

	writeStr = ""
	if sgmtstIndx != -1 and clntstIndx != -1:
		i = 0
		for element in lineSplit:
			if i != sgmtstIndx:
				writeStr += str(element).strip() + ","
			i += 1
	else:
		for element in lineSplit:
			writeStr += str(element).strip() + ","
	writeStr = writeStr[:-1] + "\n"
	outputFile.write(writeStr)

yearFile.close()
outputFile.close()