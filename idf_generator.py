# Created by Marcelo S. Olinger em 20/12/2017
# Modified by Leonardo Mazzaferro 10/04/2018
# Use Python v2.7 to run!!!
# -*- coding: utf-8 -*-


import pyidf as pf
pf.validation_level = pf.ValidationLevel.no
import logging
logging.info("start")
from pyidf.idf import IDF

import pandas as pd

import os

#original abaixo
#def main(pedireito = 3,bwidth = 20,blengthratio = 1, wwr = .25, jandorm_parlat = 0, jansala_par4 = 0, jansala_par3 = 1, jansala_par2 = 0, uh = 'bot', adiabaticsala_par2 = 0, adiabaticsala_par4 = 0, tamanhoprojecao = 0,hpav = 0, hjan = .5, azimute = 0, output = 'output.idf', path='C:\\Users\\leonardo.mazzaferro\\Documents\\Benchmark\\Sample', input = "seed.idf"):

def main(pedireito = 3,bwidth = 20,blengthratio = 1, uh = 'bot', azimute = 0, output = 'output.idf', path='C:\\Users\\leonardo.mazzaferro\\Documents\\Benchmark\\Sample', input = "seed.idf"):
	
	os.chdir(path)
	
# uh can be: bot, mid or top

	idf=IDF(input)

# Passar as variaveis numericas pra float para garantir
	bwidth = float(bwidth)
	blengthratio = float(blengthratio)
	blength = bwidth*blengthratio
	pedireito = float(pedireito)
	azimute = float(azimute)
	wwr = float(wwr)


	#ZONE LIST

	Zonas = dict()
	Zonas['Name'] = ['PZ1','PZ2','PZ3','PZ4','CORE']

	#x,y,z das Zonas
	Zonas['X'] = [0,bwidth,bwidth,0,perimetraldepth]
	Zonas['Y'] = [blength,blength,0,0,perimetraldepth]
	Zonas['Z'] = [0,0,0,0,0]

	#Surfaces
	BldgSurface = dict()
	BldgSurface['Name'] = []
	BldgSurface['SurfaceType'] =[]
	BldgSurface['ConstructionName'] = []
	BldgSurface['ZoneName'] = []
	BldgSurface['OutsideBoundryCond'] = []
	BldgSurface['OutsideBoundryCondObj'] = []
	BldgSurface['SunExposure'] = []
	BldgSurface['WindExposure'] = []
	BldgSurface['V1x'] = []
	BldgSurface['V1y'] = []
	BldgSurface['V1z'] = []
	BldgSurface['V2x'] = []
	BldgSurface['V2y'] = []
	BldgSurface['V2z'] = []
	BldgSurface['V3x'] = []
	BldgSurface['V3y'] = []
	BldgSurface['V3z'] = []
	BldgSurface['V4x'] = []
	BldgSurface['V4y'] = []
	BldgSurface['V4z'] = []

	#PZ1 - Perimetral Zone 1
	
	#ORDEM sempre Piso-Teto-1-3-2-4
	BldgSurface['Name'].append('Chao_'+Zonas['Name'][0])
	BldgSurface['Name'].append('Teto_'+Zonas['Name'][0])
	BldgSurface['Name'].append('Par1_'+Zonas['Name'][0])
	BldgSurface['Name'].append('Par3_'+Zonas['Name'][0])
	BldgSurface['Name'].append('Par2_'+Zonas['Name'][0])
	BldgSurface['Name'].append('Par4_'+Zonas['Name'][0])
	
	BldgSurface['SurfaceType'].append('Floor')
	if uh == 'top':
		BldgSurface['SurfaceType'].append('Roof')
	else:
		BldgSurface['SurfaceType'].append('Ceiling')
		
	for j in range(4):
		BldgSurface['SurfaceType'].append('Wall')
	
	# Se for a mesma construction, nao precisa

	if uh == 'bot' or uh == 'pil':
		BldgSurface['ConstructionName'].append('@@floor@@')
	else:
		BldgSurface['ConstructionName'].append('Interior Floor')
	if uh == 'top' or uh == 'uni':
		BldgSurface['ConstructionName'].append('@@roof@@')
	else:
		BldgSurface['ConstructionName'].append('InteriorCeiling')

	for j in range(6):
		BldgSurface['ZoneName'].append(Zonas['Name'][0])

	BldgSurface['ConstructionName'].append('@@paredeexterna@@')
	BldgSurface['ConstructionName'].append('Parede Interna')
	BldgSurface['ConstructionName'].append('Parede Interna')
	BldgSurface['ConstructionName'].append('@@paredeexterna@@')
	
	#PZ2 - Perimetral Zone 2
	
	BldgSurface['Name'].append('Chao_'+Zonas['Name'][1])
	BldgSurface['Name'].append('Teto_'+Zonas['Name'][1])
	BldgSurface['Name'].append('Par1_'+Zonas['Name'][1])
	BldgSurface['Name'].append('Par3_'+Zonas['Name'][1])
	BldgSurface['Name'].append('Par2_'+Zonas['Name'][1])
	BldgSurface['Name'].append('Par4_'+Zonas['Name'][1])
	
	BldgSurface['SurfaceType'].append('Floor')
	if uh == 'top' or uh == 'uni':
		BldgSurface['SurfaceType'].append('Roof')
	else:
		BldgSurface['SurfaceType'].append('Ceiling')
		
	for j in range(4):
		BldgSurface['SurfaceType'].append('Wall')
	
	# Se for o mesmo construction, nao precisa

	if uh == 'bot' or uh == 'uni' or uh == 'piu' or uh == 'pil':
		BldgSurface['ConstructionName'].append('@@floor@@')
	else:
		BldgSurface['ConstructionName'].append('Interior Floor')
	if uh == 'top' or uh == 'uni':
		BldgSurface['ConstructionName'].append('@@roof@@')
	else:
		BldgSurface['ConstructionName'].append('InteriorCeiling')

	for j in range(6):
		BldgSurface['ZoneName'].append(Zonas['Name'][1])

	BldgSurface['ConstructionName'].append('@@paredeexterna@@')
	BldgSurface['ConstructionName'].append('Parede Interna')
	BldgSurface['ConstructionName'].append('Parede Interna')
	BldgSurface['ConstructionName'].append('Parede Interna')
	
	#Dorm3
	
	BldgSurface['Name'].append('Chao_'+Zonas['Name'][2])
	BldgSurface['Name'].append('Teto_'+Zonas['Name'][2])
	BldgSurface['Name'].append('Par1_'+Zonas['Name'][2])
	BldgSurface['Name'].append('Par3_'+Zonas['Name'][2])
	BldgSurface['Name'].append('Par2_'+Zonas['Name'][2])
	BldgSurface['Name'].append('Par4_'+Zonas['Name'][2])
	
	BldgSurface['SurfaceType'].append('Floor')
	if uh == 'top' or uh == 'uni':
		BldgSurface['SurfaceType'].append('Roof')
	else:
		BldgSurface['SurfaceType'].append('Ceiling')
		
	for j in range(4):
		BldgSurface['SurfaceType'].append('Wall')
	
	# Se for a mesma construction, nao precisa

	if uh == 'bot' or uh == 'pil':
		BldgSurface['ConstructionName'].append('@@floor@@')
	else:
		BldgSurface['ConstructionName'].append('Interior Floor')
	if uh == 'top' or uh == 'uni':
		BldgSurface['ConstructionName'].append('@@roof@@')
	else:
		BldgSurface['ConstructionName'].append('InteriorCeiling')

	for j in range(6):
		BldgSurface['ZoneName'].append(Zonas['Name'][2])

	BldgSurface['ConstructionName'].append('@@paredeexterna@@')
	BldgSurface['ConstructionName'].append('Parede Interna')
	BldgSurface['ConstructionName'].append('@@paredeexterna@@')
	BldgSurface['ConstructionName'].append('Parede Interna')

	#SALA
	i = 3

	BldgSurface['Name'].append('Chao_'+Zonas['Name'][i])
	BldgSurface['Name'].append('Teto_'+Zonas['Name'][i])
	BldgSurface['Name'].append('Par11_'+Zonas['Name'][i])
	BldgSurface['Name'].append('Par12_'+Zonas['Name'][i])
	BldgSurface['Name'].append('Par13_'+Zonas['Name'][i])
	BldgSurface['Name'].append('Par3_'+Zonas['Name'][i])
	BldgSurface['Name'].append('Par2_'+Zonas['Name'][i])
	BldgSurface['Name'].append('Par4_'+Zonas['Name'][i])
	    
	BldgSurface['SurfaceType'].append('Floor')
	if uh == 'top' or uh == 'uni' or uh == 'piu':
		BldgSurface['SurfaceType'].append('Roof')
	else:
		BldgSurface['SurfaceType'].append('Ceiling')
        
	for j in range(6):
		BldgSurface['SurfaceType'].append('Wall')
    
    # Se for o mesmo construction, nao precisa
	if uh == 'bot' or uh == 'uni' or uh == 'piu' or uh == 'pil':
		BldgSurface['ConstructionName'].append('@@floor@@')
	else:
		BldgSurface['ConstructionName'].append('Interior Floor')
	if uh == 'top' or uh == 'uni':
		BldgSurface['ConstructionName'].append('@@roof@@')
	else:
		BldgSurface['ConstructionName'].append('InteriorCeiling')    

	BldgSurface['ConstructionName'].append('Parede Interna')
	BldgSurface['ConstructionName'].append('Parede Interna')
	BldgSurface['ConstructionName'].append('Parede Interna')
	BldgSurface['ConstructionName'].append('@@paredeexterna@@')
	BldgSurface['ConstructionName'].append('@@paredeexterna@@')
	BldgSurface['ConstructionName'].append('@@paredeexterna@@')
	
	for j in range(8):
		BldgSurface['ZoneName'].append(Zonas['Name'][i])

	if uh == 'uni':
		chao = 'Ground'
		teto = 'Outdoors'

	elif uh == 'bot':
		chao = 'Ground'
		teto = 'Adiabatic'

	elif uh == 'mid':
		chao = 'Adiabatic'
		teto = 'Adiabatic'

	elif uh == 'top':
		chao = 'Adiabatic'
		teto = 'Outdoors'
	
	elif uh == 'piu':
		chao = 'Outdoors'
		teto = 'Outdoors'
	
	elif uh == 'pil':
		chao = 'Outdoors'
		teto = 'Adiabatic'
	
	else:
		print('O codigo ' + str(uh) + ' nao descreve uma uh')
	
	if adiabaticsala_par4 == '1':	
		Condadiabaticsala_par4 = 'Adiabatic'
	else:
		Condadiabaticsala_par4 = 'Outdoors'
	
	if adiabaticsala_par2 == '1':	
		Condadiabaticsala_par2 = 'Adiabatic'
	else:
		Condadiabaticsala_par2 = 'Outdoors'
	
	BldgSurface['OutsideBoundryCond'] += [chao,teto,'Outdoors','Surface','Surface','Outdoors',chao,teto,'Outdoors','Surface','Surface','Surface',chao,teto,'Outdoors','Surface','Outdoors','Surface',chao,teto,'Surface','Surface','Surface','Outdoors',Condadiabaticsala_par2,Condadiabaticsala_par4]
		
	BldgSurface['OutsideBoundryCondObj'] += ['','','','Par11_Sala','Par4_Dorm2','','','','','Par12_Sala','Par4_Dorm3','Par2_Dorm1','','','','Par13_Sala','','Par2_Dorm2','','','Par3_Dorm1','Par3_Dorm2','Par3_Dorm3','','','']
         
	for i in range(len(BldgSurface['OutsideBoundryCond'])): 
	
		if uh != 'piu' or uh != 'pil':
			if BldgSurface['OutsideBoundryCond'][i] == 'Outdoors':
				BldgSurface['SunExposure'].append('SunExposed')
				BldgSurface['WindExposure'].append('WindExposed')
			else:
				BldgSurface['SunExposure'].append('NoSun')
				BldgSurface['WindExposure'].append('NoWind')
		else:
			if BldgSurface['SurfaceType'][i] == 'Floor':
				BldgSurface['SunExposure'].append('NoSun')
				BldgSurface['WindExposure'].append('WindExposed')
			else:
				if BldgSurface['OutsideBoundryCond'][i] == 'Outdoors':
					BldgSurface['SunExposure'].append('SunExposed')
					BldgSurface['WindExposure'].append('WindExposed')
				else:
					BldgSurface['SunExposure'].append('NoSun')
					BldgSurface['WindExposure'].append('NoWind')

	for i in range(3):

        #Chao
		BldgSurface['V1x'].append(DormWidth)
		BldgSurface['V1y'].append(DormLength)
		BldgSurface['V1z'].append(0)
		BldgSurface['V2x'].append(DormWidth)
		BldgSurface['V2y'].append(0)
		BldgSurface['V2z'].append(0)
		BldgSurface['V3x'].append(0)
		BldgSurface['V3y'].append(0)
		BldgSurface['V3z'].append(0)
		BldgSurface['V4x'].append(0)
		BldgSurface['V4y'].append(DormLength)
		BldgSurface['V4z'].append(0)

        #Teto
		BldgSurface['V1x'].append(0)
		BldgSurface['V1y'].append(DormLength)
		BldgSurface['V1z'].append(pedireito)
		BldgSurface['V2x'].append(0)
		BldgSurface['V2y'].append(0)
		BldgSurface['V2z'].append(pedireito)
		BldgSurface['V3x'].append(DormWidth)
		BldgSurface['V3y'].append(0)
		BldgSurface['V3z'].append(pedireito)
		BldgSurface['V4x'].append(DormWidth)
		BldgSurface['V4y'].append(DormLength)
		BldgSurface['V4z'].append(pedireito)

        #Par1
		BldgSurface['V1x'].append(DormWidth)
		BldgSurface['V1y'].append(DormLength)
		BldgSurface['V1z'].append(pedireito)
		BldgSurface['V2x'].append(DormWidth)
		BldgSurface['V2y'].append(DormLength)
		BldgSurface['V2z'].append(0)
		BldgSurface['V3x'].append(0)
		BldgSurface['V3y'].append(DormLength)
		BldgSurface['V3z'].append(0)
		BldgSurface['V4x'].append(0)
		BldgSurface['V4y'].append(DormLength)
		BldgSurface['V4z'].append(pedireito)

        #ParSul
		BldgSurface['V1x'].append(0)
		BldgSurface['V1y'].append(0)
		BldgSurface['V1z'].append(pedireito)
		BldgSurface['V2x'].append(0)
		BldgSurface['V2y'].append(0)
		BldgSurface['V2z'].append(0)
		BldgSurface['V3x'].append(DormWidth)
		BldgSurface['V3y'].append(0)
		BldgSurface['V3z'].append(0)
		BldgSurface['V4x'].append(DormWidth)
		BldgSurface['V4y'].append(0)
		BldgSurface['V4z'].append(pedireito)

        #ParLeste
		BldgSurface['V1x'].append(DormWidth)
		BldgSurface['V1y'].append(0)
		BldgSurface['V1z'].append(pedireito)
		BldgSurface['V2x'].append(DormWidth)
		BldgSurface['V2y'].append(0)
		BldgSurface['V2z'].append(0)
		BldgSurface['V3x'].append(DormWidth)
		BldgSurface['V3y'].append(DormLength)
		BldgSurface['V3z'].append(0)
		BldgSurface['V4x'].append(DormWidth)
		BldgSurface['V4y'].append(DormLength)
		BldgSurface['V4z'].append(pedireito)

        #ParOeste
		BldgSurface['V1x'].append(0)
		BldgSurface['V1y'].append(DormLength)
		BldgSurface['V1z'].append(pedireito)
		BldgSurface['V2x'].append(0)
		BldgSurface['V2y'].append(DormLength)
		BldgSurface['V2z'].append(0)
		BldgSurface['V3x'].append(0)
		BldgSurface['V3y'].append(0)
		BldgSurface['V3z'].append(0)
		BldgSurface['V4x'].append(0)
		BldgSurface['V4y'].append(0)
		BldgSurface['V4z'].append(pedireito)


	#ChaoSALA
	BldgSurface['V1x'].append(bwidth)
	BldgSurface['V1y'].append(SalaLength)
	BldgSurface['V1z'].append(0)
	BldgSurface['V2x'].append(bwidth)
	BldgSurface['V2y'].append(0)
	BldgSurface['V2z'].append(0)
	BldgSurface['V3x'].append(0)
	BldgSurface['V3y'].append(0)
	BldgSurface['V3z'].append(0)
	BldgSurface['V4x'].append(0)
	BldgSurface['V4y'].append(SalaLength)
	BldgSurface['V4z'].append(0)

	#TetoSALA
	BldgSurface['V1x'].append(0)
	BldgSurface['V1y'].append(SalaLength)
	BldgSurface['V1z'].append(pedireito)
	BldgSurface['V2x'].append(0)
	BldgSurface['V2y'].append(0)
	BldgSurface['V2z'].append(pedireito)
	BldgSurface['V3x'].append(bwidth)
	BldgSurface['V3y'].append(0)
	BldgSurface['V3z'].append(pedireito)
	BldgSurface['V4x'].append(bwidth)
	BldgSurface['V4y'].append(SalaLength)
	BldgSurface['V4z'].append(pedireito)

	#Par11SALA Norte
	BldgSurface['V1x'].append(DormWidth)
	BldgSurface['V1y'].append(SalaLength)
	BldgSurface['V1z'].append(pedireito)
	BldgSurface['V2x'].append(DormWidth)
	BldgSurface['V2y'].append(SalaLength)
	BldgSurface['V2z'].append(0)
	BldgSurface['V3x'].append(0)
	BldgSurface['V3y'].append(SalaLength)
	BldgSurface['V3z'].append(0)
	BldgSurface['V4x'].append(0)
	BldgSurface['V4y'].append(SalaLength)
	BldgSurface['V4z'].append(pedireito)

	#Par12SALA Norte
	BldgSurface['V1x'].append(2*DormWidth)
	BldgSurface['V1y'].append(SalaLength)
	BldgSurface['V1z'].append(pedireito)
	BldgSurface['V2x'].append(2*DormWidth)
	BldgSurface['V2y'].append(SalaLength)
	BldgSurface['V2z'].append(0)
	BldgSurface['V3x'].append(DormWidth)
	BldgSurface['V3y'].append(SalaLength)
	BldgSurface['V3z'].append(0)
	BldgSurface['V4x'].append(DormWidth)
	BldgSurface['V4y'].append(SalaLength)
	BldgSurface['V4z'].append(pedireito)

	#Par13SALA Norte
	BldgSurface['V1x'].append(3*DormWidth)
	BldgSurface['V1y'].append(SalaLength)
	BldgSurface['V1z'].append(pedireito)
	BldgSurface['V2x'].append(3*DormWidth)
	BldgSurface['V2y'].append(SalaLength)
	BldgSurface['V2z'].append(0)
	BldgSurface['V3x'].append(2*DormWidth)
	BldgSurface['V3y'].append(SalaLength)
	BldgSurface['V3z'].append(0)
	BldgSurface['V4x'].append(2*DormWidth)
	BldgSurface['V4y'].append(SalaLength)
	BldgSurface['V4z'].append(pedireito)

	#ParSulSALA
	BldgSurface['V1x'].append(0)
	BldgSurface['V1y'].append(0)
	BldgSurface['V1z'].append(pedireito)
	BldgSurface['V2x'].append(0)
	BldgSurface['V2y'].append(0)
	BldgSurface['V2z'].append(0)
	BldgSurface['V3x'].append(bwidth)
	BldgSurface['V3y'].append(0)
	BldgSurface['V3z'].append(0)
	BldgSurface['V4x'].append(bwidth)
	BldgSurface['V4y'].append(0)
	BldgSurface['V4z'].append(pedireito)

	#ParLesteSALA
	BldgSurface['V1x'].append(bwidth)
	BldgSurface['V1y'].append(0)
	BldgSurface['V1z'].append(pedireito)
	BldgSurface['V2x'].append(bwidth)
	BldgSurface['V2y'].append(0)
	BldgSurface['V2z'].append(0)
	BldgSurface['V3x'].append(bwidth)
	BldgSurface['V3y'].append(SalaLength)
	BldgSurface['V3z'].append(0)
	BldgSurface['V4x'].append(bwidth)
	BldgSurface['V4y'].append(SalaLength)
	BldgSurface['V4z'].append(pedireito)

	#ParOesteSALA
	BldgSurface['V1x'].append(0)
	BldgSurface['V1y'].append(SalaLength)
	BldgSurface['V1z'].append(pedireito)
	BldgSurface['V2x'].append(0)
	BldgSurface['V2y'].append(SalaLength)
	BldgSurface['V2z'].append(0)
	BldgSurface['V3x'].append(0)
	BldgSurface['V3y'].append(0)
	BldgSurface['V3z'].append(0)
	BldgSurface['V4x'].append(0)
	BldgSurface['V4y'].append(0)
	BldgSurface['V4z'].append(pedireito)

	#FenestrationSurdace:Detailed
	
	#Janelas ocupam toda a largura da facada, no meio da parede. (distancia milimetrica para nao sobrepor arestas)
	
	# FenSurface = dict()
	# FenSurface['Name'] = []
	# FenSurface['SurfaceType'] = []
	# FenSurface['ConstructionName'] = []
	# FenSurface['BuildingSurfaceName'] = []
	# FenSurface['OutsideBoundryCondObj'] = []
	# FenSurface['ShadingControlName'] = []
	# FenSurface['V1x'] = []
	# FenSurface['V1y'] = []
	# FenSurface['V1z'] = []
	# FenSurface['V2x'] = []
	# FenSurface['V2y'] = []
	# FenSurface['V2z'] = []
	# FenSurface['V3x'] = []
	# FenSurface['V3y'] = []
	# FenSurface['V3z'] = []
	# FenSurface['V4x'] = []
	# FenSurface['V4y'] = []
	# FenSurface['V4z'] = []

	# #Janelas Laterais dos Dorms
	# if jandorm_parlat == '1':
		
		# #Janela Oeste
		# FenSurface['Name'].append('JanDO')
		# FenSurface['SurfaceType'].append('Window')
		# FenSurface['ConstructionName'].append('@@vidro@@')
		# FenSurface['BuildingSurfaceName'].append('Par4_Dorm1')
		# FenSurface['OutsideBoundryCondObj'].append('')
		# FenSurface['ShadingControlName'].append('Veneziana_D1')
		# FenSurface['V1x'].append(0)
		# FenSurface['V1y'].append(ljan2SalaLength)
		# FenSurface['V1z'].append(zTopo)
		# FenSurface['V2x'].append(0)
		# FenSurface['V2y'].append(ljan2SalaLength)
		# FenSurface['V2z'].append(zBase)
		# FenSurface['V3x'].append(0)
		# FenSurface['V3y'].append(ljan1SalaLength)
		# FenSurface['V3z'].append(zBase)
		# FenSurface['V4x'].append(0)
		# FenSurface['V4y'].append(ljan1SalaLength)
		# FenSurface['V4z'].append(zTopo)

		# #Janela Leste
		# FenSurface['Name'].append('JanDL')
		# FenSurface['SurfaceType'].append('Window')
		# FenSurface['ConstructionName'].append('@@vidro@@')
		# FenSurface['BuildingSurfaceName'].append('Par2_Dorm3')
		# FenSurface['OutsideBoundryCondObj'].append('')
		# FenSurface['ShadingControlName'].append('Veneziana_D3')
		# FenSurface['V1x'].append(DormWidth)
		# FenSurface['V1y'].append(ljan1SalaLength)
		# FenSurface['V1z'].append(zTopo)
		# FenSurface['V2x'].append(DormWidth)
		# FenSurface['V2y'].append(ljan1SalaLength)
		# FenSurface['V2z'].append(zBase)
		# FenSurface['V3x'].append(DormWidth)
		# FenSurface['V3y'].append(ljan2SalaLength)
		# FenSurface['V3z'].append(zBase)
		# FenSurface['V4x'].append(DormWidth)
		# FenSurface['V4y'].append(ljan2SalaLength)
		# FenSurface['V4z'].append(zTopo)
		
	# #Janelas Dorm Norte (nos 3 Dorms)

	# for i in range(1,4):

		# FenSurface['Name'].append('JanDN'+str(i))
		# FenSurface['SurfaceType'].append('Window')
		# FenSurface['ConstructionName'].append('@@vidro@@')
		# FenSurface['BuildingSurfaceName'].append('Par1_Dorm'+str(i))
		# FenSurface['OutsideBoundryCondObj'].append('')
		# FenSurface['ShadingControlName'].append('Veneziana_D'+str(i))
		# FenSurface['V1x'].append(ljan2Dorm)
		# FenSurface['V1y'].append(DormLength)
		# FenSurface['V1z'].append(zTopo)
		# FenSurface['V2x'].append(ljan2Dorm)
		# FenSurface['V2y'].append(DormLength)
		# FenSurface['V2z'].append(zBase)
		# FenSurface['V3x'].append(ljan1Dorm)
		# FenSurface['V3y'].append(DormLength)
		# FenSurface['V3z'].append(zBase)
		# FenSurface['V4x'].append(ljan1Dorm)
		# FenSurface['V4y'].append(DormLength)
		# FenSurface['V4z'].append(zTopo)

	# #JanSO
	# if jansala_par4 == '1':

		# FenSurface['Name'].append('JanSO')
		# FenSurface['SurfaceType'].append('Window')
		# FenSurface['ConstructionName'].append('@@vidro@@')
		# FenSurface['BuildingSurfaceName'].append('Par4_Sala')
		# FenSurface['OutsideBoundryCondObj'].append('')
		# FenSurface['ShadingControlName'].append('Veneziana_Sala')
		# FenSurface['V1x'].append(0)
		# FenSurface['V1y'].append(ljan2SalaLength)
		# FenSurface['V1z'].append(zTopo)
		# FenSurface['V2x'].append(0)
		# FenSurface['V2y'].append(ljan2SalaLength)
		# FenSurface['V2z'].append(zBase)
		# FenSurface['V3x'].append(0)
		# FenSurface['V3y'].append(ljan1SalaLength)
		# FenSurface['V3z'].append(zBase)
		# FenSurface['V4x'].append(0)
		# FenSurface['V4y'].append(ljan1SalaLength)
		# FenSurface['V4z'].append(zTopo)

	# #JanSL
	# if jansala_par2 == '1':

		# FenSurface['Name'].append('JanSL')
		# FenSurface['SurfaceType'].append('Window')
		# FenSurface['ConstructionName'].append('@@vidro@@')
		# FenSurface['BuildingSurfaceName'].append('Par2_Sala')
		# FenSurface['OutsideBoundryCondObj'].append('')
		# FenSurface['ShadingControlName'].append('Veneziana_Sala')
		# FenSurface['V1x'].append(bwidth)
		# FenSurface['V1y'].append(ljan1SalaLength)
		# FenSurface['V1z'].append(zTopo)
		# FenSurface['V2x'].append(bwidth)
		# FenSurface['V2y'].append(ljan1SalaLength)
		# FenSurface['V2z'].append(zBase)
		# FenSurface['V3x'].append(bwidth)
		# FenSurface['V3y'].append(ljan2SalaLength)
		# FenSurface['V3z'].append(zBase)
		# FenSurface['V4x'].append(bwidth)
		# FenSurface['V4y'].append(ljan2SalaLength)
		# FenSurface['V4z'].append(zTopo)

	# #JanSS
	# if jansala_par3 == '1':

		# FenSurface['Name'].append('JanSS')
		# FenSurface['SurfaceType'].append('Window')
		# FenSurface['ConstructionName'].append('@@vidro@@')
		# FenSurface['BuildingSurfaceName'].append('Par3_Sala')
		# FenSurface['OutsideBoundryCondObj'].append('')
		# FenSurface['ShadingControlName'].append('Veneziana_Sala')
		# FenSurface['V1x'].append(ljan1bwidth)
		# FenSurface['V1y'].append(0)
		# FenSurface['V1z'].append(zTopo)
		# FenSurface['V2x'].append(ljan1bwidth)
		# FenSurface['V2y'].append(0)
		# FenSurface['V2z'].append(zBase)
		# FenSurface['V3x'].append(ljan2bwidth)
		# FenSurface['V3y'].append(0)
		# FenSurface['V3z'].append(zBase)
		# FenSurface['V4x'].append(ljan2bwidth)
		# FenSurface['V4y'].append(0)
		# FenSurface['V4z'].append(zTopo)

	# #Portas

	# #PortaDorm
	# for i in range(1,4):

		# FenSurface['Name'].append('PortaD'+str(i))
		# FenSurface['SurfaceType'].append('Door')
		# FenSurface['ConstructionName'].append('Porta')
		# FenSurface['BuildingSurfaceName'].append('Par3_Dorm'+str(i))
		# FenSurface['OutsideBoundryCondObj'].append('PortaS'+str(i))
		# FenSurface['ShadingControlName'].append('')
		# FenSurface['V1x'].append(x0Porta)
		# FenSurface['V1y'].append(0)
		# FenSurface['V1z'].append(hPorta)
		# FenSurface['V2x'].append(x0Porta)
		# FenSurface['V2y'].append(0)
		# FenSurface['V2z'].append(0)
		# FenSurface['V3x'].append(x0Porta+lPorta)
		# FenSurface['V3y'].append(0)
		# FenSurface['V3z'].append(0)
		# FenSurface['V4x'].append(x0Porta+lPorta)
		# FenSurface['V4y'].append(0)
		# FenSurface['V4z'].append(hPorta)

	# #PortaSala	
	# for i in range(1,4):

		# FenSurface['Name'].append('PortaS'+str(i))
		# FenSurface['SurfaceType'].append('Door')
		# FenSurface['ConstructionName'].append('Porta')
		# FenSurface['BuildingSurfaceName'].append('Par1'+str(i)+'_Sala')
		# FenSurface['OutsideBoundryCondObj'].append('PortaD'+str(i))
		# FenSurface['ShadingControlName'].append('')
		# FenSurface['V1x'].append(DormWidth*(i-1)+x0Porta+lPorta)
		# FenSurface['V1y'].append(SalaLength)
		# FenSurface['V1z'].append(hPorta)
		# FenSurface['V2x'].append(DormWidth*(i-1)+x0Porta+lPorta)
		# FenSurface['V2y'].append(SalaLength)
		# FenSurface['V2z'].append(0)
		# FenSurface['V3x'].append(DormWidth*(i-1)+x0Porta)
		# FenSurface['V3y'].append(SalaLength)
		# FenSurface['V3z'].append(0)
		# FenSurface['V4x'].append(DormWidth*(i-1)+x0Porta)
		# FenSurface['V4y'].append(SalaLength)
		# FenSurface['V4z'].append(hPorta)
		
   ########################################################################################################
 
	# if tamanhoprojecao > 0:
 
        # # Shading:Building:Detailed --------- Rayner
 
		# ShadingBuildingDetailed = {}
		# ShadingBuildingDetailed['Name'] = []
		# ShadingBuildingDetailed['Transmittance Schedule Name'] = []
		# ShadingBuildingDetailed['Number of Vertices'] = []
		# ShadingBuildingDetailed['V1x'] = []
		# ShadingBuildingDetailed['V1y'] = []
		# ShadingBuildingDetailed['V1z'] = []
		# ShadingBuildingDetailed['V2x'] = []
		# ShadingBuildingDetailed['V2y'] = []
		# ShadingBuildingDetailed['V2z'] = []
		# ShadingBuildingDetailed['V3x'] = []
		# ShadingBuildingDetailed['V3y'] = []
		# ShadingBuildingDetailed['V3z'] = []
		# ShadingBuildingDetailed['V4x'] = []
		# ShadingBuildingDetailed['V4y'] = []
		# ShadingBuildingDetailed['V4z'] = []
 
		# ShadingBuildingDetailed['Name'].append('ShadingSurfaceLeste')
		# ShadingBuildingDetailed['Transmittance Schedule Name'].append('')
		# ShadingBuildingDetailed['Number of Vertices'].append(4)
		# ShadingBuildingDetailed['V1x'].append(DormWidth+2*DormWidth+tamanhoprojecao) 
		# ShadingBuildingDetailed['V1y'].append(0)
		# ShadingBuildingDetailed['V1z'].append(pedireito+hpav)                            
		# ShadingBuildingDetailed['V2x'].append(DormWidth+2*DormWidth+tamanhoprojecao)
		# ShadingBuildingDetailed['V2y'].append(SalaLength+DormLength)        
		# ShadingBuildingDetailed['V2z'].append(pedireito+hpav)
		# ShadingBuildingDetailed['V3x'].append(DormWidth+2*DormWidth)                    
		# ShadingBuildingDetailed['V3y'].append(SalaLength+DormLength)
		# ShadingBuildingDetailed['V3z'].append(pedireito+hpav)
		# ShadingBuildingDetailed['V4x'].append(DormWidth+2*DormWidth)
		# ShadingBuildingDetailed['V4y'].append(0)
		# ShadingBuildingDetailed['V4z'].append(pedireito+hpav)
 
		# ShadingBuildingDetailed['Name'].append('ShadingSurfaceOeste')
		# ShadingBuildingDetailed['Transmittance Schedule Name'].append('')
		# ShadingBuildingDetailed['Number of Vertices'].append(4)
		# ShadingBuildingDetailed['V1x'].append(0)
		# ShadingBuildingDetailed['V1y'].append(SalaLength+DormLength)
		# ShadingBuildingDetailed['V1z'].append(pedireito+hpav)
		# ShadingBuildingDetailed['V2x'].append(0)
		# ShadingBuildingDetailed['V2y'].append(0)
		# ShadingBuildingDetailed['V2z'].append(pedireito+hpav)
		# ShadingBuildingDetailed['V3x'].append(-tamanhoprojecao)                 
		# ShadingBuildingDetailed['V3y'].append(0)
		# ShadingBuildingDetailed['V3z'].append(pedireito+hpav)
		# ShadingBuildingDetailed['V4x'].append(-tamanhoprojecao)
		# ShadingBuildingDetailed['V4y'].append(SalaLength+DormLength)
		# ShadingBuildingDetailed['V4z'].append(pedireito+hpav)
 
		# ShadingBuildingDetailed['Name'].append('ShadingSurfaceNorte')
		# ShadingBuildingDetailed['Transmittance Schedule Name'].append('')
		# ShadingBuildingDetailed['Number of Vertices'].append(4)
		# ShadingBuildingDetailed['V1x'].append(DormWidth+2*DormWidth+tamanhoprojecao)
		# ShadingBuildingDetailed['V1y'].append(SalaLength+DormLength+tamanhoprojecao)    
		# ShadingBuildingDetailed['V1z'].append(pedireito+hpav)
		# ShadingBuildingDetailed['V2x'].append(DormWidth+2*DormWidth+tamanhoprojecao)
		# ShadingBuildingDetailed['V2y'].append(SalaLength+DormLength)
		# ShadingBuildingDetailed['V2z'].append(pedireito+hpav)
		# ShadingBuildingDetailed['V3x'].append(-tamanhoprojecao)
		# ShadingBuildingDetailed['V3y'].append(SalaLength+DormLength)
		# ShadingBuildingDetailed['V3z'].append(pedireito+hpav)
		# ShadingBuildingDetailed['V4x'].append(-tamanhoprojecao)
		# ShadingBuildingDetailed['V4y'].append(SalaLength+DormLength+tamanhoprojecao)
		# ShadingBuildingDetailed['V4z'].append(pedireito+hpav)
 
		# ShadingBuildingDetailed['Name'].append('ShadingSurfaceSul')
		# ShadingBuildingDetailed['Transmittance Schedule Name'].append('')
		# ShadingBuildingDetailed['Number of Vertices'].append(4)
		# ShadingBuildingDetailed['V1x'].append(DormWidth+2*DormWidth+tamanhoprojecao)
		# ShadingBuildingDetailed['V1y'].append(0)
		# ShadingBuildingDetailed['V1z'].append(pedireito+hpav)
		# ShadingBuildingDetailed['V2x'].append(DormWidth+2*DormWidth+tamanhoprojecao)
		# ShadingBuildingDetailed['V2y'].append(-tamanhoprojecao)
		# ShadingBuildingDetailed['V2z'].append(pedireito+hpav)
		# ShadingBuildingDetailed['V3x'].append(-tamanhoprojecao)
		# ShadingBuildingDetailed['V3y'].append(-tamanhoprojecao)
		# ShadingBuildingDetailed['V3z'].append(pedireito+hpav)
		# ShadingBuildingDetailed['V4x'].append(-tamanhoprojecao)
		# ShadingBuildingDetailed['V4y'].append(0)
		# ShadingBuildingDetailed['V4z'].append(pedireito+hpav)
 
     
    ########################################################################################################
    	####################ADICIONA NO IDF###################################################################################

	for i in range(len(BldgSurface['Name'])):
	    obj = IDF._create_datadict("BuildingSurface:Detailed")
	    obj['Name'] = BldgSurface['Name'][i]
	    obj['Surface Type'] = BldgSurface['SurfaceType'][i]
	    obj['Construction Name'] = BldgSurface['ConstructionName'][i]
	    obj['Zone Name'] = BldgSurface['ZoneName'][i]
	    obj['Outside Boundary Condition'] = BldgSurface['OutsideBoundryCond'][i]
	    obj['Outside Boundary Condition Object'] = BldgSurface['OutsideBoundryCondObj'][i]
	    obj['Sun Exposure'] = BldgSurface['SunExposure'][i]
	    obj['Wind Exposure'] = BldgSurface['WindExposure'][i]
	    obj['Number of Vertices'] = 4
	    obj[u'Vertex 1 X-coordinate', 0] = BldgSurface['V1x'][i]
	    obj[u'Vertex 1 Y-coordinate', 0] = BldgSurface['V1y'][i]
	    obj[u'Vertex 1 Z-coordinate', 0] = BldgSurface['V1z'][i]
	    obj[u'Vertex 1 X-coordinate', 1] = BldgSurface['V2x'][i]
	    obj[u'Vertex 1 Y-coordinate', 1] = BldgSurface['V2y'][i]
	    obj[u'Vertex 1 Z-coordinate', 1] = BldgSurface['V2z'][i]
	    obj[u'Vertex 1 X-coordinate', 2] = BldgSurface['V3x'][i]
	    obj[u'Vertex 1 Y-coordinate', 2] = BldgSurface['V3y'][i]
	    obj[u'Vertex 1 Z-coordinate', 2] = BldgSurface['V3z'][i]
	    obj[u'Vertex 1 X-coordinate', 3] = BldgSurface['V4x'][i]
	    obj[u'Vertex 1 Y-coordinate', 3] = BldgSurface['V4y'][i]
	    obj[u'Vertex 1 Z-coordinate', 3] = BldgSurface['V4z'][i]  
	    idf.add(obj)

	for i in range(len(FenSurface['Name'])):
		obj = IDF._create_datadict("FenestrationSurface:Detailed")
		obj["Name"] = FenSurface['Name'][i]
		obj["Surface Type"] = FenSurface['SurfaceType'][i]
		obj["Construction Name"] = FenSurface["ConstructionName"][i]
		obj["Building Surface Name"] = FenSurface['BuildingSurfaceName'][i]
		obj["Outside Boundary Condition Object"] = FenSurface['OutsideBoundryCondObj'][i]
		obj["Shading Control Name"] = FenSurface['ShadingControlName'][i]
		obj['Number of Vertices'] = 4
		obj['Vertex 1 X-coordinate'] = FenSurface['V1x'][i]
		obj['Vertex 1 Y-coordinate'] = FenSurface['V1y'][i]
		obj['Vertex 1 Z-coordinate'] = FenSurface['V1z'][i]
		obj['Vertex 2 X-coordinate'] = FenSurface['V2x'][i]
		obj['Vertex 2 Y-coordinate'] = FenSurface['V2y'][i]
		obj['Vertex 2 Z-coordinate'] = FenSurface['V2z'][i]
		obj['Vertex 3 X-coordinate'] = FenSurface['V3x'][i]
		obj['Vertex 3 Y-coordinate'] = FenSurface['V3y'][i]
		obj['Vertex 3 Z-coordinate'] = FenSurface['V3z'][i]
		obj['Vertex 4 X-coordinate'] = FenSurface['V4x'][i]
		obj['Vertex 4 Y-coordinate'] = FenSurface['V4y'][i]
		obj['Vertex 4 Z-coordinate'] = FenSurface['V4z'][i] 
		idf.add(obj)
  ########################################################## Rayner
	if tamanhoprojecao > 0:  
		for i in range(len(ShadingBuildingDetailed['Name'])):
			obj = IDF._create_datadict('Shading:Building:Detailed')
			obj['Name'] = ShadingBuildingDetailed['Name'][i]
			obj['Transmittance Schedule Name'] = ShadingBuildingDetailed['Transmittance Schedule Name'][i]
			obj['Number of Vertices'] = 4
			obj[u'Vertex 1 X-coordinate', 0] = ShadingBuildingDetailed['V1x'][i]
			obj[u'Vertex 1 Y-coordinate', 0] = ShadingBuildingDetailed['V1y'][i]
			obj[u'Vertex 1 Z-coordinate', 0] = ShadingBuildingDetailed['V1z'][i]
			obj[u'Vertex 1 X-coordinate', 1] = ShadingBuildingDetailed['V2x'][i]
			obj[u'Vertex 1 Y-coordinate', 1] = ShadingBuildingDetailed['V2y'][i]
			obj[u'Vertex 1 Z-coordinate', 1] = ShadingBuildingDetailed['V2z'][i]
			obj[u'Vertex 1 X-coordinate', 2] = ShadingBuildingDetailed['V3x'][i]
			obj[u'Vertex 1 Y-coordinate', 2] = ShadingBuildingDetailed['V3y'][i]
			obj[u'Vertex 1 Z-coordinate', 2] = ShadingBuildingDetailed['V3z'][i]
			obj[u'Vertex 1 X-coordinate', 3] = ShadingBuildingDetailed['V4x'][i]
			obj[u'Vertex 1 Y-coordinate', 3] = ShadingBuildingDetailed['V4y'][i]
			obj[u'Vertex 1 Z-coordinate', 3] = ShadingBuildingDetailed['V4z'][i]
			idf.add(obj)

    ##################################################################		
	for i in range(len(Zonas['Name'])):
		obj = IDF._create_datadict('Zone')
		obj['Name'] = Zonas['Name'][i]
		obj['Direction of Relative North'] = 0
		obj['Multiplier'] = 1
		obj['X Origin'] = Zonas['X'][i]
		obj['Y Origin'] = Zonas['Y'][i]
		obj['Z Origin'] = Zonas['Z'][i] 
		idf.add(obj)


	
	obj = IDF._create_datadict('Building')
	obj['Name'] = output #(str(pedireito)+'-'+str(bwidth)+'-'+str(bwidth)+'-'+str(wwr)+'-'+str(uh)+'-'+str(Adiabatic))
	obj['North Axis'] = azimute
	obj['Terrain'] = 'City'
	obj['Solar Distribution'] = 'FullInteriorAndExterior'
	obj['Loads Convergence Tolerance Value'] = .5
	obj['Temperature Convergence Tolerance Value'] = .5
	idf.add(obj)


	out = [idf, output]

	return(out)
	
def idfFunc(baseFile):
    idf = open(baseFile, 'r')
    return idf.read()
	
def sampleGen(file = 'sample.csv', path='C:\\Users\\leonardo.mazzaferro\\Documents\\Benchmark\\Sample'):
	
	os.chdir(path)
	condition = False
	i = 0
	
	dadoSample = pd.read_csv(file)
	with open(file,'r') as file_read:				
		lines = file_read.readlines()
	
	for line in lines:
		if condition == True:
			
			line = line.split(',')
			
			pedireito = line[0]
			bwidth = line[1]
			blengthratio = line[2]
			wwr = line[3]
			jandorm_parlat = line[4]
			jansala_par4 = line[5]
			jansala_par3 = line[6]
			jansala_par2 = line[7]
			uh = line[8]
			adiabaticsala_par2 = line[9]
			adiabaticsala_par4 = line[10]
			tamanhoprojecao = line[11]
			hpav = line[12]
			hjan = line[13]
			azimute = line[14]
			caso = '{:04.0f}'.format(i)
			output = ('caso_{}.idf'.format(caso))
			print(output)
			out = main(pedireito, bwidth, blengthratio, wwr, uh, azimute, output , path)
					  #pedireito, bwidth, blengthratio, wwr, jandorm_parlat, jansala_par4, jansala_par3, jansala_par2, uh, adiabaticsala_par2, adiabaticsala_par4, tamanhoprojecao, hpav, hjan, azimute, output, path, input
			idf = out[0]
			outputname = out[1]
			idf.save(outputname)
			
			#baseFile = outputname
			idfBase = idfFunc(outputname)
			
			#arquivo contendo a amostragem gerada pelo e++
			#dadoSample = pd.read_csv(file)

			# lista contendo strings com o nome dos parametros amostrados
			variaveis = dadoSample.keys()
			#print(variaveis)
			
			for j in variaveis:
				# para cada parametro amostrado vai procurar o nome da variavel no idfBase e substituir
				if "@@" in j:
					idfBase = idfBase.replace(j, str(dadoSample[j][i-1]))
				# eu nao testei o ## nesse codigo mas acredito que funcione... Aqui ele substitui o conteudo do arquivo que a variavel indica
				if "!##" in j:
				
					with open(dadoSample[j][i-1],'r') as file:				
						conteudo = file.read()
					idfBase = idfBase.replace(j, conteudo)
			# aqui vai escrever num idf a string que foi modificada na linha anterior tendo o nome da linha do sample.csv correspondente
			with open(outputname, 'w') as file:
				file.write(idfBase)
		condition = True
		i += 1

sampleGen(path='C:\\Users\\leonardo.mazzaferro\\Documents\\Benchmark\\Sample')