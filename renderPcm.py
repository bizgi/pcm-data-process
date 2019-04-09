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


def getCase(path, caseNum):
#	path = 'pcmDataMerged.csv'
#	path = 'pcmDataSteFo1.csv'
	
	df = pd.read_csv(path).astype(str)
	delta = pd.DataFrame.from_records(df)
	
	q1 = delta['case'] == caseNum
	case = delta[q1]
#	print (case)
	return case


def plot(plotCase):

#	path = plotCase['path']
	cases = plotCase['cases']
	caseLabel = plotCase['caseLabel']
	param = plotCase['param']
	xLabel = plotCase['xLabel']
	yLabel = plotCase['yLabel']
	text = plotCase['text']
	
	text2 = plotCase['text2']
	textx = plotCase['textx']
	texty =plotCase['texty']
	
	marker = ['o', 'd', '*', 'v', '1', '2', '3', '^', '3', 'v', '^', 'h', 'd']
	dash = [[2,1,10,2], [2,2], [6,4], [4,4], [1,1]]
	
	plt.figure(figsize=(6,6))
	
	xMax = []
	yMax = []

	for i in range(len(cases)):
		x = np.array(getCase(path, cases[i])['t']).astype(float)
		y = np.array(getCase(path, cases[i])[param]).astype(float)
		xMax.append(x.max())
		yMax.append(y.max())
	
	xm = np.array(xMax).astype(float)
	ym = np.array(yMax).astype(float)
	
	for i in range(len(cases)):
		x = np.array(getCase(path, cases[i])['t']).astype(float)
		y = np.array(getCase(path, cases[i])[param]).astype(float)
		if text == 'Gr':
			x = x * 10
			plt.xlim(-0.05,1.80)
		if 'hFlux' in param:
			x = np.delete(x, (0,1))
			y = np.delete(y, (0,1)) / 1000
			
			plt.ylim(-0.08, 3.58)
#		print (x, y)	 
		plt.plot(x,y, label= caseLabel[i], dashes=dash[i])
#		plt.plot (makeSpline(x, y)[0], makeSpline(x, y)[1], label= caseLabel[i],  dashes=dash[i])
		
#		dx = np.interp(x, (0, xm.max()), (0,1))
#		dy = np.interp(y, (0, ym.max()), (0,1))
#		plt.plot(dx,dy, label= caseLabel[i])

	plt.text(textx, texty, text2)
	plt.rcParams.update({'font.size': 11})
#	SMALL_SIZE = 13
#	plt.rc('font', size=12)
	plt.rc('axes', titlesize=14)
	plt.rc('axes', labelsize=14)
	plt.rc('xtick', labelsize=14)
	plt.rc('ytick', labelsize=14)
	
#	plt.ylim(-0.1, 10.1)

#	ax2.set_ylabel('s')
	plt.legend(loc=0)
#	plt.xlim(18, 39)
	plt.xlabel(xLabel)
#	plt.xlabel('T [$^o$C]')
	plt.ylabel(yLabel)
	plt.tight_layout()
	

#	plt.scatter(x0, y0, label='Experiment (Erdemir, D., 2016)', color = 'C2')

#	plt.plot(x4, y, label='CFD - 441111 Mesh', color = 'C5', dashes=[5,1])
#	plt.plot(x5, y, label='CFD - 686656 Mesh', color = 'C7', dashes=[9,4])
#	
#	plt.plot(x01, y01, label='Numerical (Zachar, A., 2003)', color = 'C9')
	
#	plt.text(0.7 , 0.05, '$T_{ini}$ = 41 $^oC$ \n $T_{in}$ = 20 $^oC$ \n Q = 1.6 L/min \n t = 1500 s \n\n')
	
#	plt.text(0.6 , 0.04, r'$ T* = \frac{ T - T_{in} }  { T_{ini} - T_{in} }$', fontsize=18)
	

#	plt.scatter(x0, y0, label='Experiment (Knudsen, S., 2004)', color = 'C0')


	sName = param + '-' + text
#	plt.savefig('.\imgPcm\\'+ sName + '.png', format='png', dpi=300)


wallTempMf = {
		'cases' : ['Case-1', 'Case-2', 'Case-3'],
		'caseLabel' : ['C1, $T_{w}$-$T_{m}$ = 5$^oC$, $Gr_D$ = 4.18x10$^3$, Ste = 0.06', 'C2, $T_{w}$-$T_{m}$ = 10$^oC$, $Gr_D$ = 8.37x10$^3$, Ste = 0.119', 'C3, $T_{w}$-$T_{m}$ = 15$^oC$, $Gr_D$ = 1.26x10$^4$, Ste = 0.179'],
		'text' : 'wall-temp', 
		'text2' : 'D = 0.015m, H = 0.5m',
		'textx' : 7,
		'texty' : 0.2,
		'param' : 'Mf',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Melt Fraction',
		}

wallTempNu = {
		'cases' : ['Case-1', 'Case-2', 'Case-3'],
		'caseLabel' : ['C1, $T_{w}$-$T_{m}$ = 5$^oC$, $Gr_D$ = 4.18x10$^3$, Ste = 0.06', 'C2, $T_{w}$-$T_{m}$ = 10$^oC$, $Gr_D$ = 8.37x10$^3$, Ste = 0.119', 'C3, $T_{w}$-$T_{m}$ = 15$^oC$, $Gr_D$ = 1.26x10$^4$, Ste = 0.179'],
		'text' : 'wall-temp',
		'text2' : 'D = 0.015m, H = 0.5m',
		'textx' : 7,
		'texty' : 2.7,
		'param' : 'hFluxSide',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Heat Flux [kW/m$^2$]',
		}

SteMf = {
		'cases' : ['Case-5', 'Case-2', 'Case-4'],
		'caseLabel' : ['C5, Ste = 0.098, $T_{w}$-$T_{m}$ = 8.25$^oC$, D = 0.016m', 'C2, Ste = 0.119, $T_{w}$-$T_{m}$ = 10$^oC$, D = 0.015m', 'C4, Ste = 0.146, $T_{w}$-$T_{m}$ = 12.3$^oC$, D = 0.014m'],
		'text' : 'Ste', 
		'text2' : 'Gr$_D$ = 8.37 x 10$^3$, H = 0.5m', 
		'textx' : 5.2,
		'texty' : 0.2,
		'param' : 'Mf',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Melt Fraction',
		}

SteNu = {
		'cases' : ['Case-5', 'Case-2', 'Case-4'],
		'caseLabel' : ['C5, Ste = 0.098, $T_{w}$-$T_{m}$ = 8.25$^oC$, D = 0.016m', 'C2, Ste = 0.119, $T_{w}$-$T_{m}$ = 10$^oC$, D = 0.015m', 'C4, Ste = 0.146, $T_{w}$-$T_{m}$ = 12.3$^oC$, D = 0.014m'],
		'text' : 'Ste', 
		'text2' : 'Gr$_D$ = 8.37 x 10$^3$, H = 0.5m',
		'textx' : 5.2,
		'texty' : 2.7,
		'param' : 'hFlux',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Heat Flux [kW/m$^2$]',
		}

GrDMf = {
		'cases' : ['Case-2', 'Case-6', 'Case-7'],
		'caseLabel' : ['C2, Gr$_D$ = 8.37x$10^3$, D = 0.015m', 'C6, Gr$_D$ = 1.98x$10^4$, D = 0.020m', 'C7, Gr$_D$ = 3.87x$10^4$, D = 0.025m'],
		'text' : 'Gr', 
		'text2' : 'Ste = 0.119, $T_{w}$-$T_{m}$ = 10$^oC$, H = 0.5m',
		'textx' : 0.70,
		'texty' : 0.2,
		'param' : 'Mf',
		'xLabel' : 'SteFo x$10^{-1}$',
		'yLabel' : 'Melt Fraction',
		}

GrDNu = {
		'cases' : ['Case-2', 'Case-6', 'Case-7'],
		'caseLabel' : ['C2, Gr$_D$ = 8.37x$10^3$, D = 0.015m', 'C6, Gr$_D$ = 1.98x$10^4$, D = 0.020m', 'C7, Gr$_D$ = 3.87x$10^4$, D = 0.025m'],
		'text' : 'Gr', 
		'text2' : 'Ste = 0.119, $T_{w}$-$T_{m}$ = 10$^oC$, H = 0.5m',
		'textx' : 0.65,
		'texty' : 2.6,
		'param' : 'hFlux',
		'xLabel' : 'SteFo x$10^{-1}$',
		'yLabel' : 'Heat Flux [kW/m$^2$]',
		}


DMf = {
		'cases' : ['Case-2', 'Case-6', 'Case-7'],
		'caseLabel' : ['C2, D = 0.015m, Gr$_D$ = 8.37x$10^3$', 'C6, D = 0.020m, Gr$_D$ = 1.98x$10^4$', 'C7, D = 0.025m, Gr$_D$ = 3.87x$10^4$'],
		'text' : 'D',
		'text2' : 'Ste = 0.119, $T_{w}$-$T_{m}$ = 10$^oC$, H = 0.5m',
		'textx' : 5.5,
		'texty' : 0.2,
		'param' : 'Mf',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Melt Fraction',
		}

DNu = {
		'cases' : ['Case-2', 'Case-6', 'Case-7'],
		'caseLabel' : ['C2, D = 0.015m, Gr$_D$ = 8.37x$10^3$', 'C6, D = 0.020m, Gr$_D$ = 1.98x$10^4$', 'C7, D = 0.025m, Gr$_D$ = 3.87x$10^4$'],
		'text' : 'D',
		'text2' : 'Ste = 0.119, $T_{w}$-$T_{m}$ = 10$^oC$, H = 0.5m',
		'textx' : 5.5,
		'texty' : 2.7,
		'param' : 'hFlux',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Heat Flux [kW/m$^2$]',
		}


HMf = {
		'cases' : ['Case-8', 'Case-6', 'Case-9'],
		'caseLabel' : ['C8, H = 0.25m', 'C6, H = 0.50m', 'C9 H = 0.75m'],
		'text' : 'H', 
		'text2' : 'Ste = 0.119, $T_{w}$-$T_{m}$ = 10$^oC$, D = 0.020m',
		'textx' : 3,
		'texty' : 0.1,
		'param' : 'Mf',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Melt Fraction',
		}

HNu = {
		'cases' : ['Case-8', 'Case-6', 'Case-9'],
		'caseLabel' : ['C8, H = 0.25m', 'C6, H = 0.50m', 'C9 H = 0.75m'],
		'text' : 'H',
		'text2' : 'Ste = 0.119, $T_{w}$-$T_{m}$ = 10$^oC$, D = 0.020m', 
		'textx' : 4.4,
		'texty' : 2.7,
		'param' : 'hFlux',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Heat Flux [kW/m$^2$]',
		}



DHMf = {
		'cases' : ['Case-2', 'Case-6', 'Case-7', 'Case-8'],
		'caseLabel' : ['D/H = 0.03', 'D/H = 0.04','D/H = 0.05','D/H = 0.08'],
		'text' : 'DH',
		'text2' : 'Ste = 0.119, $T_{w}$-$T_{m}$ = 10$^oC$', 
		'textx' : 8,
		'texty' : 0.3,
		'param' : 'Mf',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Melt Fraction',
		}

DHNu = {
		'cases' : [ 'Case-2', 'Case-6', 'Case-7', 'Case-8'],
		'caseLabel' : ['D/H = 0.03', 'D/H = 0.04','D/H = 0.05','D/H = 0.08'],
		'text' : 'DH', 
		'text2' : 'Ste = 0.119, $T_{w}$-$T_{m}$ = 10$^oC$', 
		'textx' : 8,
		'texty' : 0.3,
		'param' : 'hFlux',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Heat Flux [kW/m$^2$]',
		}


kShellMf = {
		'cases' : ['Case-11', 'Case-10', 'Case-8'],
		'caseLabel' : ['C11, k* = 0.429', 'C10, k* = 0.987', 'C8, k* = 0.999'],
		'text' : 'kShell',
		'text2' : 'Ste = 0.119, Gr$_D$ = 1.98x$10^4$, $T_{w}$-$T_{m}$ = 10$^oC$', 
		'textx' : 4,
		'texty' : 0.1,
		'param' : 'Mf',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Melt Fraction',
		}

kShellNu = {
		'cases' : ['Case-11', 'Case-10', 'Case-8'],
		'caseLabel' : ['C11, k* = 0.429', 'C10, k* = 0.987', 'C8, k* = 0.999'],
		'text' : 'kShell',
		'text2' : 'Ste = 0.119, Gr$_D$ = 1.98x$10^4$, $T_{w}$-$T_{m}$ = 10$^oC$',
		'textx' : 4,
		'texty' : 2.7,
		'param' : 'hFlux',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Heat Flux [kW/m$^2$]',
		}


sCoolMf = {
		'cases' : ['Case-8', 'Case-12', 'Case-13'],
		'caseLabel' : ['C8, $T_{ini}$* = 0.02160', 'C12, $T_{ini}$* = 0.04938', 'C13, $T_{ini}$* = 0.08025'],
		'text' : 'sCool', 
		'text2' : 'Ste = 0.119, Gr$_D$ = 1.98x$10^4$, $T_{w}$-$T_{m}$ = 10$^oC$ \n\n D = 0.020m, H = 0.25m',
		'textx' : 2.9,
		'texty' : 0.1,
		'param' : 'Mf',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Melt Fraction',
		}

sCoolNu = {
		'cases' : ['Case-8', 'Case-12', 'Case-13'],
		'caseLabel' : ['C8, $T_{ini}$* = 0.02160', 'C12, $T_{ini}$* = 0.04938', 'C13, $T_{ini}$* = 0.08025'],
		'text' : 'sCool', 
		'text2' : 'Ste = 0.119, Gr$_D$ = 1.98x$10^4$, $T_{w}$-$T_{m}$ = 10$^oC$ \n\n D = 0.020m, H = 0.25m',
		'textx' : 2.9,
		'texty' : 2.5,
		'param' : 'hFlux',
		'xLabel' : 'Time [min]',
		'yLabel' : 'Heat Flux [kW/m$^2$]',
		}



#path = 'pcmDataSteFoMerged.csv'
path = 'pcmDataMerged.csv'
#
#plot(GrDMf)
#plot(GrDNu)


#plot(wallTempMf)
plot(wallTempNu)
###
#plot(SteMf)
#plot(SteNu)
##
#plot(DMf)
#plot(DNu)

#plot(HMf)
#plot(HNu)
#
#plot(DHMf)
#plot(DHNu)
##
#plot(kShellMf)
#plot(kShellNu)
#
#plot(sCoolMf)
#plot(sCoolNu)
