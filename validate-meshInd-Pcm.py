# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:31:48 2018

@author: izgib
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
import pandas as pd

def makeSpline(x, y):
	t, c, k = interpolate.splrep(x , y, s=0, k=2)
	xSmooth = np.linspace(min(x), max(x), 200)
#		spline = interpolate.BSpline(t, c, k, extrapolate=False)
	spline = interpolate.CubicSpline(x , y, bc_type='natural')
	ySmooth = spline(xSmooth)
#		print(ySmooth)
	ys2 = []
#		for i in range(len(ySmooth)) :
#			if (ySmooth[i] < 0):
#				yy = 0
##				yy = 0.9999
#			else:
#				yy = ySmooth[i]
#			
##			print(yy)
#			ys2.append(yy)
	
	
	return xSmooth, ySmooth

	
def dless(n):
	o = np.interp(n, (n.min(), n.max()), (0 ,1))
	return o


def validate():
	path = 'pcm-validate-ebadi.csv'
		
	df = pd.read_csv(path).astype(str)
	delta = pd.DataFrame.from_records(df)
	
	q1 = delta['case'] == 'cfd'
	case1 = delta[q1]
	
#	q2 = delta['C'].str.match('m2')
#	case2 = delta[q2]
#	
#	q3 = delta['C'].str.match('m3')
#	case3 = delta[q3]
#	
	q4 = delta['case'] == 'exp5'
	case4 = delta[q4]
#	
	q5 = delta['case'] == 'exp-5'
	case5 = delta[q5]
	
	q2 = delta['case'] == 'exp'
	case2 = delta[q2]
	
	q3 = delta['case'] == 'num'
	case3 = delta[q3]
#	print(case1X, case1Y)

	
	y_ = np.array(case1['mf']).astype(float)	
	y2_ = np.array(case2['mf']).astype(float)	
	y3_ = np.array(case3['mf']).astype(float)	
	y4_ = np.array(case4['mf']).astype(float)
	y4_ = np.array(case5['mf']).astype(float)
	
	x1 = np.array(case1['t']).astype(float)
	x2 = np.array(case2['t']).astype(float)
	x3 = np.array(case3['t']).astype(float)
	x4 = np.array(case4['t']).astype(float)
	x5 = np.array(case5['t']).astype(float)
	
	y = dless(y_)
	y2 = dless(y2_)
	y3 = dless(y3_)
	
#	y4 = np.array(case4['mf']).astype(float)
#	y5 = np.array(case5['mf']).astype(float)
#	
#	y0 = np.array(case6['Z']).astype(float)	
#	x0 = np.array(case6['T']).astype(float)
#	
#	y01 = np.array(case7['Z']).astype(float)	
#	x01 = np.array(case7['T']).astype(float)
##	print(y0, x0)
	plt.figure(figsize=(6,6))
	
#	fig, ax1 = plt.subplots(figsize=(5,8))

	plt.rcParams.update({'font.size': 12})
#	SMALL_SIZE = 13
#	plt.rc('font', size=12)
	plt.rc('axes', titlesize=14)
	plt.rc('axes', labelsize=14)
	plt.rc('xtick', labelsize=14)
	plt.rc('ytick', labelsize=14)
#	ax2 = ax1.twinx()
#	plt.scatter(x0, y0, label='Experiment (Erdemir, D., 2016)', color = 'C2')
	
	plt.plot(makeSpline(x1, y_)[0], makeSpline(x1, y_)[1], label='CFD (This study)', color = 'C0', )
	plt.scatter(x2, y2_, label='Experimental (Ebadi, S. et al, 2018)', color = 'C1')	
	plt.plot(makeSpline(x3, y3_)[0], makeSpline(x3, y3_)[1], label='Numerical (Ebadi, S. et al, 2018)', color = 'C1', dashes=[1,1])	
	
#	plt.plot(makeSpline(x4, y4_)[0], makeSpline(x4, y4_)[1], label='5%', color = 'C5', )
	
#	plt.plot(x2, y4, label='CFD - 441111 Mesh', color = 'C5', dashes=[5,1])
#	plt.plot(x2, y5, label='CFD - 686656 Mesh', color = 'C7', dashes=[9,4])
#	
#	plt.plot(x01, y01, label='Numerical (Zachar, A., 2003)', color = 'C9')
	
#	plt.text(0.7 , 0.05, '$T_{ini}$ = 41 $^oC$ \n $T_{in}$ = 20 $^oC$ \n Q = 1.6 L/min \n t = 1500 s \n\n')
	
#	plt.text(0.6 , 0.04, r'$ T* = \frac{ T - T_{in} }  { T_{ini} - T_{in} }$', fontsize=18)
	

#	plt.scatter(x0, y0, label='Experiment (Knudsen, S., 2004)', color = 'C0')
#	
#	plt.plot(x1, y, label='CFD - 70171 Mesh', color = 'C2', dashes=[1,1])
#	plt.plot(x2, y, label='CFD - 101507 Mesh', color = 'C1', dashes=[2,2])	
#	plt.plot(x3, y, label='CFD - 132071 Mesh', color = 'C3')	
#	plt.plot(x4, y, label='CFD - 154933 Mesh', color = 'C5', dashes=[5,1])


#	ax2.scatter(x2, yy, color='C8', label='Mesh')
	
#	ax2.set_ylabel('s')
	plt.legend(loc=0)
	plt.ylim(-0.05, 1.05)
	plt.xlabel('Time [min]')
#	plt.xlabel('T [$^o$C]')
	plt.ylabel('Melt Fraction')
	plt.tight_layout()
#	plot.legend(loc=0)
	sName = path
#	plt.savefig('.\imgPcm\\'+ sName + '.png', format='png', dpi=300)
#	
	
	
def meshInd():
 
	path = 'pcm-mesh-ind.csv'
		
	df = pd.read_csv(path).astype(str)
#	print (df)
	delta = pd.DataFrame.from_records(df)
	
	q1 = delta['mesh'] == '16k'
	case1 = delta[q1]
	
	q2 = delta['mesh'] == '24k'
	case2 = delta[q2]
	
	q3 = delta['mesh'] == '36k'
	case3 = delta[q3]
	
#	q4 = delta['case'].str.match('284k')
#	case4 = delta[q4]
	
#	q5 = delta['case'].str.match('324k')
#	case5 = delta[q5]
	
#	q6 = delta['case'].str.match('390k')
#	case6 = delta[q6]
#	
	
	x = np.array(case1['t']).astype(float)
	y1 = np.array(case1['mf']).astype(float)
	y2 = np.array(case2['mf']).astype(float)
	y3 = np.array(case3['mf']).astype(float)
#	x4 = np.array(case4['T']).astype(float)
#	x5 = np.array(case5['T']).astype(float)
#	x6 = np.array(case6['T']).astype(float)
	
#	y = dless(y_)
#	x1 = dless(x1_)
#	x2 = dless(x2_)
#	x3 = dless(x3_)
#	x4 = dless(x4_)
#	x5 = dless(x5_)

	
#	print (x1)

#	y0 = np.array(case6['Z']).astype(float)	
#	x0 = np.array(case6['T']).astype(float)
#	
#	y01 = np.array(case7['Z']).astype(float)	
#	x01 = np.array(case7['T']).astype(float)
##	print(y0, x0)
	plt.figure(figsize=(6,6))
	
#	fig, ax1 = plt.subplots(figsize=(6,6))

	plt.rcParams.update({'font.size': 12})
#	SMALL_SIZE = 13
#	plt.rc('font', size=12)
	plt.rc('axes', titlesize=14)
	plt.rc('axes', labelsize=14)
	plt.rc('xtick', labelsize=14)
	plt.rc('ytick', labelsize=14)
#	ax2 = ax1.twinx()
#	plt.scatter(x0, y0, label='Experiment (Erdemir, D., 2016)', color = 'C2')
	
	plt.plot(x, y1, label='16k cells', color = 'C0', dashes=[1,1,9,2] )
	plt.plot(x, y2, label='24k cells', color = 'C3')	
	plt.plot(x, y3, label='36k cells', color = 'C2', dashes=[2,1])	
#	plt.plot(x4, y, label='284b Hücre', color = 'C3')
#	plt.plot(x5, y, label='324b Hücre', color = 'C4', dashes=[1,1])
#	plt.plot(x6, y, label='390b Hücre', color = 'C5', dashes=[2,2])
#	
	
#	plt.text(0.5 , 0.04, r'$ T* = \frac{ T - T_{min} }  { T_{max} - T_{min} }$', fontsize=18)
	
#	plt.plot(x01, y01, label='Numerical (Zachar, A., 2003)', color = 'C9')
	
#	plt.text(0.7 , 0.05, '$T_{ini}$ = 41 $^oC$ \n $T_{in}$ = 20 $^oC$ \n Q = 1.6 L/min \n t = 1500 s \n\n')
	
#	plt.text(0.7 , 0.04, r'$ T* = \frac{ T - T_{in} }  { T_{ini} - T_{in} }$', fontsize=15)
	

#	plt.scatter(x0, y0, label='Experiment (Knudsen, S., 2004)', color = 'C0')
#	
#	plt.plot(x1, y, label='147b Mesh', color = 'C5', dashes=[1,1] )
#	plt.plot(x2, y, label='198b Mesh', color = 'C1',dashes=[2,2])	
#	plt.plot(x3, y, label='250b Mesh', color = 'C0')	
#	plt.plot(x4, y, label='298b Mesh', color = 'C1', dashes=[5,1])
#	plt.plot(x5, y, label='324b Mesh', color = 'C7', dashes=[9,4])


#	ax2.scatter(x2, yy, color='C8', label='Mesh')
	
#	ax2.set_ylabel('s')
	plt.legend(loc=0)
	plt.xlim(-0.2, 5.2)
	plt.ylim(-0.05, 1.05)
	plt.xlabel('Time [min]')
#	plt.xlabel('T [$^o$C]')
	plt.ylabel('Melt Fraction')
	plt.tight_layout()
#	plot.legend(loc=0)
	sName = path
#	plt.savefig('.\imgPcm\\'+ sName + '.png', format='png', dpi=300)
	
	
meshInd()


	
validate()