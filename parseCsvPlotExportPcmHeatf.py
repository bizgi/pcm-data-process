# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:50:05 2018

@author: izgib
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
import csv
import os
import pandas as pd

#dataFolder = '.\pcmData\csvDataPcmSteFo30'

dataFolder = ['.\pcmData\csvDataPcm', '.\pcmData\csvDataPcm30', '.\pcmData\csvDataPcmSteFo', '.\pcmData\csvDataPcmSteFo30']

#dataFolderTout = 'csvDataPcm'

def parse(dataFolder):
#		print (data)
	t = []
	Mf = []
	hFlux = []
	hFluxTop = []
	hFluxSide = []
	hFluxBottom = []
	case = []
	
	files = os.listdir('.\\'+ dataFolder)
	for name in files:
	#	print(name)
		path = '.\\' + dataFolder + '\\' + name
	#	print(path)
	#	print(data[1])
	
		caseNum = path.split('\\')[-1].split('.')[0].split('--')[-1]
#		print(caseNum)

	
		with open(path, 'r') as f:
			reader = csv.reader(f, delimiter=',')
			data = list(reader)
#			print (data)
			
			for i in range(len(data)):
				if 'Series 1 at mfr' in data[i]:
					print (data[i])
					j = 4
					while True:
						print(caseNum, i, j)
#						print (data[i+j])
						if data[i+j] == []:
							break
						case.append(caseNum)
						if 'SteFo' in dataFolder:
							t.append(data[i+j][0])
						else:							
							t.append((round(((float(data[i+j][0]))/60),2)))

						Mf.append(round(float(data[i+j][1]),4))

						j=j+1
					print ('mf-break')
				
				elif 'Series 2 at heatf' in data[i]:
					print (data[i])
					j = 4
					while True:
						print(caseNum, i, j)
#						print (data[i+j])
						if data[i+j] == []:
							break
#						case.append(caseNum)
#						t.append((round(((float(data[i+j][0]))/60),2)))
						hFlux.append(round(float(data[i+j][1]),4))

						j=j+1
					print ('Nu-break')		
					
				elif 'Series 3 at heatft' in data[i]:
					print (data[i])
					j = 4
					while True:
						print(caseNum, i, j)
#						print (data[i+j])
						if data[i+j] == []:
							break
#						case.append(caseNum)
#						t.append((round(((float(data[i+j][0]))/60),2)))
						hFluxTop.append(round(float(data[i+j][1]),4))

						j=j+1
					print ('Nu-break') 		
					
				elif 'Series 4 at heatfs' in data[i]:
					print (data[i])
					j = 4
					while True:
						print(caseNum, i, j)
#						print (data[i+j])
						if data[i+j] == []:
							break
#						case.append(caseNum)
#						t.append((round(((float(data[i+j][0]))/60),2)))
						hFluxSide.append(round(float(data[i+j][1]),4))

						j=j+1
					print ('Nu-break') 
					
				elif 'Series 5 at heatfb' in data[i]:
					print (data[i])
					j = 4
					while True:
						print(caseNum, i, j)
#						print (data[i+j])
						if data[i+j] == []:
							break
#						case.append(caseNum)
#						t.append((round(((float(data[i+j][0]))/60),2)))
						hFluxBottom.append(round(float(data[i+j][1]),4))

						j=j+1
					print ('Nu-break') 			

	 					
#			print(t)
#			print(Mf)
#			print(Nu)
#			print(len(Mf))
	return (t, Mf, hFlux, hFluxTop, hFluxSide, hFluxBottom, case)





def writeData(data, name):
	with open(name, "w", newline='') as csv_file:
		writer = csv.writer(csv_file, delimiter=',' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
		header = ['t', 'Mf', 'hFlux', 'hFluxTop','hFluxSide','hFluxBottom', 'case']
		writer.writerow(header)

		for i in range(len(data[1])):
			wData = [data[0][i], data[1][i], data[2][i], data[3][i], data[4][i], data[5][i], data[6][i]]
			print(wData)
			writer.writerow(wData)
		

#
#writeData(data)
#
		
def mergeData(path, path2, name):
#	path = 'pcmData0.csv'
#	path2 = 'pcmData1.csv'
	
	df = pd.read_csv(path).astype(str)
	delta = pd.DataFrame.from_records(df)
	
	df2 = pd.read_csv(path2).astype(str)
	delta2 = pd.DataFrame.from_records(df2)
	
#	print (delta)
#	pcmDataMerged =[]
	for i in range(1,14) :
		q1 = delta['case'] == 'Case-' + str(i)
		q2 = delta2['case'] == 'Case-' + str(i)

		case = delta[q1][3:]
		case2 = delta2[q2].append(case)
#		print (case)
		print (case2)
#		pcmDataMerged.append(case2)
	
		case2.to_csv(name,  mode='a', encoding='utf-8', index=False)
#	print(pcmDataMerged)
	os.remove(path)
	os.remove(path2)
	return
		

#mergeData()
		

for i in range(len(dataFolder)):
	data = parse(dataFolder[i])
	name = 'pcmData'+str(i)+'.csv'
	writeData(data, name)
	if i == 1:
		mergeData('pcmData0.csv', 'pcmData1.csv', 'pcmDataMerged.csv')
	elif i == 3:
		mergeData('pcmData2.csv', 'pcmData3.csv', 'pcmDataSteFoMerged.csv')


		
		
		