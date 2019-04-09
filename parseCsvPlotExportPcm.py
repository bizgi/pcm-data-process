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

dataFolder = '.\pcmData\csvDataPcmSteFo30'
#dataFolderTout = 'csvDataPcm'

def parse(dataFolder):
#		print (data)
	t = []
	Mf = []
	Nu = []
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
						
#						t.append((round(((float(data[i+j][0]))/60),2)))
						t.append(data[i+j][0])
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
						Nu.append(round(float(data[i+j][1]),4))

						j=j+1
					print ('Nu-break')						
 			

	 					
			print(t)
			print(Mf)
			print(Nu)
#			print(len(Mf))
	return (t, Mf, Nu, case)



#data = parse(dataFolder)




def writeData(data):
	with open('pcmData2.csv', "w", newline='') as csv_file:
		writer = csv.writer(csv_file, delimiter=',' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
		header = ['t', 'Mf', 'Nu', 'case']
		writer.writerow(header)

		for i in range(len(data[1])):
			wData = [data[0][i], data[1][i], data[2][i], data[3][i]]
			print(wData)
			writer.writerow(wData)
		


#
#writeData(data)
#
		
def mergeData():
	path = 'pcmData1.csv'
	path2 = 'pcmData2.csv'
	
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
	
		case2.to_csv('pcmDataSteFoMerged.csv',  mode='a', encoding='utf-8', index=False)
#	print(pcmDataMerged)
	return
		

#mergeData()
		
		
		
		
		