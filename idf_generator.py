# RUN USING ONLY Python v2.7!!!
# -*- coding: utf-8 -*-


import pyidf as pf
pf.validation_level = pf.ValidationLevel.no
import logging
logging.info("start")
from pyidf.idf import IDF

import pandas as pd
import os

def main(shell_depth = 5, ceiling_height = 3,building_xlen = 20, building_ratio = 1, wwr = .25, boundaries = 'bot', shading = 0, hpav = 0, azimuth = 0, output = 'output.idf', path='C:/Users/Marcelo/gits/idf_generator', input = "seed.idf"):
    
    os.chdir(path)
    idf=IDF(input)

    # Passar as variaveis numericas pra float soh pra garantir
    shell_depth = float(shell_depth)
    building_xlen = float(building_xlen)
    building_ratio = float(building_ratio)
    building_ylen = building_xlen*building_ratio
    ceiling_height = float(ceiling_height)
    hpav = float(hpav)
    azimuth = float(azimuth)
    wwr = float(wwr)
    shading = float(shading)

    #variaveis dependentes

    window_z1 = ceiling_height*(1-wwr)/2
    window_z2 = window_z1+(ceiling_height*wwr)
    window_x1 = building_xlen*.001
    window_x2 = building_xlen*.999
    window_y1 = building_ylen*.001
    window_y2 = building_ylen*.999

    #Lista das Zones

    Zones = dict()
    Zones['Name'] = ['PZ1','PZ2','PZ3','PZ4','CORE']

    #x,y,z das Zones
    Zones['X'] = [0,0,building_xlen,building_xlen,shell_depth]
    Zones['Y'] = [building_ylen,0,0,building_ylen,shell_depth]
    Zones['Z'] = [hpav,hpav,hpav,hpav,hpav]

    #Surfaces

    BldgSurface = dict()
    BldgSurface['Name'] = []
    BldgSurface['SurfaceType'] =[]
    BldgSurface['ConstructionName'] = []
    BldgSurface['ZoneName'] = []
    BldgSurface['OutsideBoundaryCond'] = []
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

    #### PZ (Perimetral Zones) ####
    
    # PZ1 -------------------------------------------
    
    #Order Always: Floor, Ceiling, 1, 2, 3, 4
    BldgSurface['Name'].append('Floor_'+Zones['Name'][0])
    BldgSurface['Name'].append('Ceiling_'+Zones['Name'][0])
    BldgSurface['Name'].append('Wall1_'+Zones['Name'][0])
    BldgSurface['Name'].append('Wall2_'+Zones['Name'][0])
    BldgSurface['Name'].append('Wall3_'+Zones['Name'][0])
    BldgSurface['Name'].append('Wall4_'+Zones['Name'][0])
    
    BldgSurface['SurfaceType'].append('Floor')
    if boundaries == 'top' or boundaries == 'exp':
        BldgSurface['SurfaceType'].append('Roof')
    else:
        BldgSurface['SurfaceType'].append('Ceiling')
        
    for j in range(4):
        BldgSurface['SurfaceType'].append('Wall')
    
    # Se for o mesmo construction, nao precisa

    if boundaries == 'bot' or boundaries == 'exp' or boundaries == 'pex' or boundaries == 'pad':
        BldgSurface['ConstructionName'].append('@@floor@@')
    else:
        BldgSurface['ConstructionName'].append('Interior Floor')
    if boundaries == 'top' or boundaries == 'exp':
        BldgSurface['ConstructionName'].append('@@roof@@')
    else:
        BldgSurface['ConstructionName'].append('InteriorCeiling')

    for j in range(6):
        BldgSurface['ZoneName'].append(Zones['Name'][0])

    BldgSurface['ConstructionName'].append('@@paredeexterna@@')
    BldgSurface['ConstructionName'].append('Parede Interna')
    BldgSurface['ConstructionName'].append('Parede Interna')
    BldgSurface['ConstructionName'].append('Parede Interna')
    
    # PZ2 -------------------------------------------
    
    BldgSurface['Name'].append('Floor_'+Zones['Name'][1])
    BldgSurface['Name'].append('Ceiling_'+Zones['Name'][1])
    BldgSurface['Name'].append('Wall1_'+Zones['Name'][1])
    BldgSurface['Name'].append('Wall2_'+Zones['Name'][1])
    BldgSurface['Name'].append('Wall3_'+Zones['Name'][1])
    BldgSurface['Name'].append('Wall4_'+Zones['Name'][1])
    
    BldgSurface['SurfaceType'].append('Floor')
    if boundaries == 'top' or boundaries == 'exp':
        BldgSurface['SurfaceType'].append('Roof')
    else:
        BldgSurface['SurfaceType'].append('Ceiling')
        
    for j in range(4):
        BldgSurface['SurfaceType'].append('Wall')
    
    # Se for o mesmo construction, nao precisa

    if boundaries == 'bot' or boundaries == 'exp' or boundaries == 'pex' or boundaries == 'pad':
        BldgSurface['ConstructionName'].append('@@floor@@')
    else:
        BldgSurface['ConstructionName'].append('Interior Floor')
    if boundaries == 'top' or boundaries == 'exp':
        BldgSurface['ConstructionName'].append('@@roof@@')
    else:
        BldgSurface['ConstructionName'].append('InteriorCeiling')

    for j in range(6):
        BldgSurface['ZoneName'].append(Zones['Name'][1])

    BldgSurface['ConstructionName'].append('@@paredeexterna@@')
    BldgSurface['ConstructionName'].append('Parede Interna')
    BldgSurface['ConstructionName'].append('Parede Interna')
    BldgSurface['ConstructionName'].append('Parede Interna')
    
    # PZ3 -------------------------------------------
    
    BldgSurface['Name'].append('Floor_'+Zones['Name'][2])
    BldgSurface['Name'].append('Ceiling_'+Zones['Name'][2])
    BldgSurface['Name'].append('Wall1_'+Zones['Name'][2])
    BldgSurface['Name'].append('Wall2_'+Zones['Name'][2])
    BldgSurface['Name'].append('Wall3_'+Zones['Name'][2])
    BldgSurface['Name'].append('Wall4_'+Zones['Name'][2])
    
    BldgSurface['SurfaceType'].append('Floor')
    if boundaries == 'top' or boundaries == 'exp':
        BldgSurface['SurfaceType'].append('Roof')
    else:
        BldgSurface['SurfaceType'].append('Ceiling')
        
    for j in range(4):
        BldgSurface['SurfaceType'].append('Wall')
    
    # Se for o mesmo construction, nao precisa

    if boundaries == 'bot' or boundaries == 'exp' or boundaries == 'pex' or boundaries == 'pad':
        BldgSurface['ConstructionName'].append('@@floor@@')
    else:
        BldgSurface['ConstructionName'].append('Interior Floor')
    if boundaries == 'top' or boundaries == 'exp':
        BldgSurface['ConstructionName'].append('@@roof@@')
    else:
        BldgSurface['ConstructionName'].append('InteriorCeiling')

    for j in range(6):
        BldgSurface['ZoneName'].append(Zones['Name'][2])

    BldgSurface['ConstructionName'].append('@@paredeexterna@@')
    BldgSurface['ConstructionName'].append('Parede Interna')
    BldgSurface['ConstructionName'].append('Parede Interna')
    BldgSurface['ConstructionName'].append('Parede Interna')

    
    # PZ4 -------------------------------------------
    
    BldgSurface['Name'].append('Floor_'+Zones['Name'][3])
    BldgSurface['Name'].append('Ceiling_'+Zones['Name'][3])
    BldgSurface['Name'].append('Wall1_'+Zones['Name'][3])
    BldgSurface['Name'].append('Wall2_'+Zones['Name'][3])
    BldgSurface['Name'].append('Wall3_'+Zones['Name'][3])
    BldgSurface['Name'].append('Wall4_'+Zones['Name'][3])
    
    BldgSurface['SurfaceType'].append('Floor')
    if boundaries == 'top' or boundaries == 'exp':
        BldgSurface['SurfaceType'].append('Roof')
    else:
        BldgSurface['SurfaceType'].append('Ceiling')
        
    for j in range(4):
        BldgSurface['SurfaceType'].append('Wall')
    
    # Se for o mesmo construction, nao precisa

    if boundaries == 'bot' or boundaries == 'exp' or boundaries == 'pex' or boundaries == 'pad':
        BldgSurface['ConstructionName'].append('@@floor@@')
    else:
        BldgSurface['ConstructionName'].append('Interior Floor')
    if boundaries == 'top' or boundaries == 'exp':
        BldgSurface['ConstructionName'].append('@@roof@@')
    else:
        BldgSurface['ConstructionName'].append('InteriorCeiling')

    for j in range(6):
        BldgSurface['ZoneName'].append(Zones['Name'][3])

    BldgSurface['ConstructionName'].append('@@paredeexterna@@')
    BldgSurface['ConstructionName'].append('Parede Interna')
    BldgSurface['ConstructionName'].append('Parede Interna')
    BldgSurface['ConstructionName'].append('Parede Interna')

    # CORE --------------------------------------------------------
    
    BldgSurface['Name'].append('Floor_'+Zones['Name'][4])
    BldgSurface['Name'].append('Ceiling_'+Zones['Name'][4])
    BldgSurface['Name'].append('Wall1_'+Zones['Name'][4])
    BldgSurface['Name'].append('Wall2_'+Zones['Name'][4])
    BldgSurface['Name'].append('Wall3_'+Zones['Name'][4])
    BldgSurface['Name'].append('Wall4_'+Zones['Name'][4])
        
    BldgSurface['SurfaceType'].append('Floor')
    if boundaries == 'top' or boundaries == 'exp' or boundaries == 'pex':
        BldgSurface['SurfaceType'].append('Roof')
    else:
        BldgSurface['SurfaceType'].append('Ceiling')
        
    for j in range(6):
        BldgSurface['SurfaceType'].append('Wall')
    
    # Se for o mesmo construction, nao precisa
    if boundaries == 'bot' or boundaries == 'exp' or boundaries == 'pex' or boundaries == 'pad':
        BldgSurface['ConstructionName'].append('@@floor@@')
    else:
        BldgSurface['ConstructionName'].append('Interior Floor')
    if boundaries == 'top' or boundaries == 'exp':
        BldgSurface['ConstructionName'].append('@@roof@@')
    else:
        BldgSurface['ConstructionName'].append('InteriorCeiling')
    
    for j in range(6):
        BldgSurface['ZoneName'].append(Zones['Name'][4])  

    BldgSurface['ConstructionName'].append('Parede Interna')
    BldgSurface['ConstructionName'].append('Parede Interna')
    BldgSurface['ConstructionName'].append('Parede Interna')
    BldgSurface['ConstructionName'].append('Parede Interna')

    #ALL ZONES... ------------------------------------------
    
    if boundaries == 'exp':
        floor = 'Ground'
        ceiling = 'Outdoors'

    elif boundaries == 'bot':
        floor = 'Ground'
        ceiling = 'Adiabatic'

    elif boundaries == 'mid':
        floor = 'Adiabatic'
        ceiling = 'Adiabatic'

    elif boundaries == 'top':
        floor = 'Adiabatic'
        ceiling = 'Outdoors'
    
    elif boundaries == 'pex':
        floor = 'Outdoors'
        ceiling = 'Outdoors'
    
    elif boundaries == 'pad':
        floor = 'Outdoors'
        ceiling = 'Adiabatic'
    
    else:
        print('The code ' + str(boundaries) + ' is not valid.')
    
    BldgSurface['OutsideBoundaryCond'] += [floor,ceiling,'Outdoors','Surface','Surface','Surface',floor,ceiling,'Outdoors','Surface','Surface','Surface',floor,ceiling,'Outdoors','Surface','Surface','Surface',floor,ceiling,'Outdoors','Surface','Surface','Surface',floor,ceiling,'Surface','Surface','Surface','Surface']
        
    BldgSurface['OutsideBoundryCondObj'] += ['','','','Wall4_PZ2','Wall1_CORE','Wall2_PZ4','','','','Wall4_PZ3','Wall2_CORE','Wall2_PZ1','','','','Wall4_PZ4','Wall3_CORE','Wall2_PZ2','','','','Wall4_PZ1','Wall4_CORE','Wall2_PZ3','','','Wall3_PZ1','Wall3_PZ2','Wall3_PZ3','Wall3_PZ4']
         
    for i in range(len(BldgSurface['OutsideBoundaryCond'])): 
    
        if boundaries != 'pex' or boundaries != 'pad':
            if BldgSurface['OutsideBoundaryCond'][i] == 'Outdoors':
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
                if BldgSurface['OutsideBoundaryCond'][i] == 'Outdoors':
                    BldgSurface['SunExposure'].append('SunExposed')
                    BldgSurface['WindExposure'].append('WindExposed')
                else:
                    BldgSurface['SunExposure'].append('NoSun')
                    BldgSurface['WindExposure'].append('NoWind')
    
    # Geometry -----------------------------------------------
    
    ## PZ1

    #Floor
    BldgSurface['V1x'].append(building_xlen)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(0)
    BldgSurface['V2x'].append(building_xlen-shell_depth)
    BldgSurface['V2y'].append(-shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(shell_depth)
    BldgSurface['V3y'].append(-shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(0)

    #Ceiling
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(shell_depth)
    BldgSurface['V2y'].append(-shell_depth)
    BldgSurface['V2z'].append(ceiling_height)
    BldgSurface['V3x'].append(building_xlen-shell_depth)
    BldgSurface['V3y'].append(-shell_depth)
    BldgSurface['V3z'].append(ceiling_height)
    BldgSurface['V4x'].append(building_xlen)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall1
    BldgSurface['V1x'].append(building_xlen)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(building_xlen)
    BldgSurface['V2y'].append(0)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(0)
    BldgSurface['V3y'].append(0)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall2
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(0)
    BldgSurface['V2y'].append(0)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(shell_depth)
    BldgSurface['V3y'].append(-shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(shell_depth)
    BldgSurface['V4y'].append(-shell_depth)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall3
    BldgSurface['V1x'].append(shell_depth)
    BldgSurface['V1y'].append(-shell_depth)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(shell_depth)
    BldgSurface['V2y'].append(-shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(building_xlen-shell_depth)
    BldgSurface['V3y'].append(-shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(building_xlen-shell_depth)
    BldgSurface['V4y'].append(-shell_depth)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall4
    BldgSurface['V1x'].append(building_xlen-shell_depth)
    BldgSurface['V1y'].append(-shell_depth)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(building_xlen-shell_depth)
    BldgSurface['V2y'].append(-shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(building_xlen)
    BldgSurface['V3y'].append(0)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(building_xlen)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(ceiling_height)

    ## PZ2

    #Floor
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(building_ylen)
    BldgSurface['V1z'].append(0)
    BldgSurface['V2x'].append(shell_depth)
    BldgSurface['V2y'].append(building_ylen-shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(shell_depth)
    BldgSurface['V3y'].append(shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(0)

    #Ceiling
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(shell_depth)
    BldgSurface['V2y'].append(shell_depth)
    BldgSurface['V2z'].append(ceiling_height)
    BldgSurface['V3x'].append(shell_depth)
    BldgSurface['V3y'].append(building_ylen-shell_depth)
    BldgSurface['V3z'].append(ceiling_height)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(building_ylen)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall1
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(building_ylen)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(0)
    BldgSurface['V2y'].append(building_ylen)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(0)
    BldgSurface['V3y'].append(0)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall2
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(0)
    BldgSurface['V2y'].append(0)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(shell_depth)
    BldgSurface['V3y'].append(shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(shell_depth)
    BldgSurface['V4y'].append(shell_depth)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall3
    BldgSurface['V1x'].append(shell_depth)
    BldgSurface['V1y'].append(shell_depth)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(shell_depth)
    BldgSurface['V2y'].append(shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(shell_depth)
    BldgSurface['V3y'].append(building_ylen-shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(shell_depth)
    BldgSurface['V4y'].append(building_ylen-shell_depth)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall4
    BldgSurface['V1x'].append(shell_depth)
    BldgSurface['V1y'].append(building_ylen-shell_depth)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(shell_depth)
    BldgSurface['V2y'].append(building_ylen-shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(0)
    BldgSurface['V3y'].append(building_ylen)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(building_ylen)
    BldgSurface['V4z'].append(ceiling_height)
    
    ## PZ3

    #Floor
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(0)
    BldgSurface['V2x'].append(-building_xlen)
    BldgSurface['V2y'].append(0)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(-building_xlen+shell_depth)
    BldgSurface['V3y'].append(shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(-shell_depth)
    BldgSurface['V4y'].append(shell_depth)
    BldgSurface['V4z'].append(0)

    #Ceiling
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(-shell_depth)
    BldgSurface['V2y'].append(shell_depth)
    BldgSurface['V2z'].append(ceiling_height)
    BldgSurface['V3x'].append(-building_xlen+shell_depth)
    BldgSurface['V3y'].append(shell_depth)
    BldgSurface['V3z'].append(ceiling_height)
    BldgSurface['V4x'].append(-building_xlen)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall1
    BldgSurface['V1x'].append(-building_xlen)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(-building_xlen)
    BldgSurface['V2y'].append(0)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(0)
    BldgSurface['V3y'].append(0)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall2
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(0)
    BldgSurface['V2y'].append(0)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(-shell_depth)
    BldgSurface['V3y'].append(shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(-shell_depth)
    BldgSurface['V4y'].append(shell_depth)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall3
    BldgSurface['V1x'].append(-shell_depth)
    BldgSurface['V1y'].append(shell_depth)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(-shell_depth)
    BldgSurface['V2y'].append(shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(-building_xlen+shell_depth)
    BldgSurface['V3y'].append(shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(-building_xlen+shell_depth)
    BldgSurface['V4y'].append(shell_depth)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall4
    BldgSurface['V1x'].append(-building_xlen+shell_depth)
    BldgSurface['V1y'].append(shell_depth)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(-building_xlen+shell_depth)
    BldgSurface['V2y'].append(shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(-building_xlen)
    BldgSurface['V3y'].append(0)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(-building_xlen)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(ceiling_height)

    ## PZ4

    #Floor
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(-building_ylen)
    BldgSurface['V1z'].append(0)
    BldgSurface['V2x'].append(-shell_depth)
    BldgSurface['V2y'].append(-building_ylen+shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(-shell_depth)
    BldgSurface['V3y'].append(-shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(0)

    #Ceiling
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(-shell_depth)
    BldgSurface['V2y'].append(-shell_depth)
    BldgSurface['V2z'].append(ceiling_height)
    BldgSurface['V3x'].append(-shell_depth)
    BldgSurface['V3y'].append(-building_ylen+shell_depth)
    BldgSurface['V3z'].append(ceiling_height)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(-building_ylen)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall1
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(-building_ylen)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(0)
    BldgSurface['V2y'].append(-building_ylen)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(0)
    BldgSurface['V3y'].append(0)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall2
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(0)
    BldgSurface['V2y'].append(0)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(-shell_depth)
    BldgSurface['V3y'].append(-shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(-shell_depth)
    BldgSurface['V4y'].append(-shell_depth)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall3
    BldgSurface['V1x'].append(-shell_depth)
    BldgSurface['V1y'].append(-shell_depth)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(-shell_depth)
    BldgSurface['V2y'].append(-shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(-shell_depth)
    BldgSurface['V3y'].append(-building_ylen+shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(-shell_depth)
    BldgSurface['V4y'].append(-building_ylen+shell_depth)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall4
    BldgSurface['V1x'].append(-shell_depth)
    BldgSurface['V1y'].append(-building_ylen+shell_depth)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(-shell_depth)
    BldgSurface['V2y'].append(-building_ylen+shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(0)
    BldgSurface['V3y'].append(-building_ylen)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(-building_ylen)
    BldgSurface['V4z'].append(ceiling_height)

    ## CORE

    #Floor
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(0)
    BldgSurface['V2x'].append(0)
    BldgSurface['V2y'].append(building_ylen-2*shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(building_xlen-2*shell_depth)
    BldgSurface['V3y'].append(building_ylen-2*shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(building_xlen-2*shell_depth)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(0)

    #Ceiling
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(building_xlen-2*shell_depth)
    BldgSurface['V2y'].append(0)
    BldgSurface['V2z'].append(ceiling_height)
    BldgSurface['V3x'].append(building_xlen-2*shell_depth)
    BldgSurface['V3y'].append(building_ylen-2*shell_depth)
    BldgSurface['V3z'].append(ceiling_height)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(building_ylen-2*shell_depth)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall1
    BldgSurface['V1x'].append(building_xlen-2*shell_depth)
    BldgSurface['V1y'].append(building_ylen-2*shell_depth)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(building_xlen-2*shell_depth)
    BldgSurface['V2y'].append(building_ylen-2*shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(0)
    BldgSurface['V3y'].append(building_ylen-2*shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(building_ylen-2*shell_depth)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall2
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(building_ylen-2*shell_depth)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(0)
    BldgSurface['V2y'].append(building_ylen-2*shell_depth)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(0)
    BldgSurface['V3y'].append(0)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(0)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall3
    BldgSurface['V1x'].append(0)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(0)
    BldgSurface['V2y'].append(0)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(building_xlen-2*shell_depth)
    BldgSurface['V3y'].append(0)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(building_xlen-2*shell_depth)
    BldgSurface['V4y'].append(0)
    BldgSurface['V4z'].append(ceiling_height)

    #Wall4
    BldgSurface['V1x'].append(building_xlen-2*shell_depth)
    BldgSurface['V1y'].append(0)
    BldgSurface['V1z'].append(ceiling_height)
    BldgSurface['V2x'].append(building_xlen-2*shell_depth)
    BldgSurface['V2y'].append(0)
    BldgSurface['V2z'].append(0)
    BldgSurface['V3x'].append(building_xlen-2*shell_depth)
    BldgSurface['V3y'].append(building_ylen-2*shell_depth)
    BldgSurface['V3z'].append(0)
    BldgSurface['V4x'].append(building_xlen-2*shell_depth)
    BldgSurface['V4y'].append(building_ylen-2*shell_depth)
    BldgSurface['V4z'].append(ceiling_height)

    ##### FenestrationSurdace:Detailed ---------------------------------------------------------------
    
    #Janelas ocupam toda a largura da facada, no meio da parede. (distancia milimetrica para nao sobrepor arestas)
    
    FenSurface = dict()
    FenSurface['Name'] = []
    FenSurface['SurfaceType'] = []
    FenSurface['ConstructionName'] = []
    FenSurface['BuildingSurfaceName'] = []
    FenSurface['OutsideBoundryCondObj'] = []
    FenSurface['ShadingControlName'] = []
    FenSurface['V1x'] = []
    FenSurface['V1y'] = []
    FenSurface['V1z'] = []
    FenSurface['V2x'] = []
    FenSurface['V2y'] = []
    FenSurface['V2z'] = []
    FenSurface['V3x'] = []
    FenSurface['V3y'] = []
    FenSurface['V3z'] = []
    FenSurface['V4x'] = []
    FenSurface['V4y'] = []
    FenSurface['V4z'] = []

    ## Create Windows
        
    # PZ1 Window
    
    FenSurface['Name'].append('Window_PZ1')
    FenSurface['SurfaceType'].append('Window')
    FenSurface['ConstructionName'].append('@@vidro@@')
    FenSurface['BuildingSurfaceName'].append('Wall1_PZ1')
    FenSurface['OutsideBoundryCondObj'].append('')
    FenSurface['ShadingControlName'].append('')
    FenSurface['V1x'].append(window_x2)
    FenSurface['V1y'].append(0)
    FenSurface['V1z'].append(window_z2)
    FenSurface['V2x'].append(window_x2)
    FenSurface['V2y'].append(0)
    FenSurface['V2z'].append(window_z1)
    FenSurface['V3x'].append(window_x1)
    FenSurface['V3y'].append(0)
    FenSurface['V3z'].append(window_z1)
    FenSurface['V4x'].append(window_x1)
    FenSurface['V4y'].append(0)
    FenSurface['V4z'].append(window_z2)

        
    # PZ2 Window
    
    FenSurface['Name'].append('Window_PZ2')
    FenSurface['SurfaceType'].append('Window')
    FenSurface['ConstructionName'].append('@@vidro@@')
    FenSurface['BuildingSurfaceName'].append('Wall1_PZ2')
    FenSurface['OutsideBoundryCondObj'].append('')
    FenSurface['ShadingControlName'].append('')
    FenSurface['V1x'].append(0)
    FenSurface['V1y'].append(window_y2)
    FenSurface['V1z'].append(window_z2)
    FenSurface['V2x'].append(0)
    FenSurface['V2y'].append(window_y2)
    FenSurface['V2z'].append(window_z1)
    FenSurface['V3x'].append(0)
    FenSurface['V3y'].append(window_y1)
    FenSurface['V3z'].append(window_z1)
    FenSurface['V4x'].append(0)
    FenSurface['V4y'].append(window_y1)
    FenSurface['V4z'].append(window_z2)
        
    # PZ3 Window
    
    FenSurface['Name'].append('Window_PZ3')
    FenSurface['SurfaceType'].append('Window')
    FenSurface['ConstructionName'].append('@@vidro@@')
    FenSurface['BuildingSurfaceName'].append('Wall1_PZ3')
    FenSurface['OutsideBoundryCondObj'].append('')
    FenSurface['ShadingControlName'].append('')
    FenSurface['V1x'].append(-window_x2)
    FenSurface['V1y'].append(0)
    FenSurface['V1z'].append(window_z2)
    FenSurface['V2x'].append(-window_x2)
    FenSurface['V2y'].append(0)
    FenSurface['V2z'].append(window_z1)
    FenSurface['V3x'].append(-window_x1)
    FenSurface['V3y'].append(0)
    FenSurface['V3z'].append(window_z1)
    FenSurface['V4x'].append(-window_x1)
    FenSurface['V4y'].append(0)
    FenSurface['V4z'].append(window_z2)

        
    # PZ4 Window
    
    FenSurface['Name'].append('Window_PZ4')
    FenSurface['SurfaceType'].append('Window')
    FenSurface['ConstructionName'].append('@@vidro@@')
    FenSurface['BuildingSurfaceName'].append('Wall1_PZ4')
    FenSurface['OutsideBoundryCondObj'].append('')
    FenSurface['ShadingControlName'].append('')
    FenSurface['V1x'].append(0)
    FenSurface['V1y'].append(-window_y2)
    FenSurface['V1z'].append(window_z2)
    FenSurface['V2x'].append(0)
    FenSurface['V2y'].append(-window_y2)
    FenSurface['V2z'].append(window_z1)
    FenSurface['V3x'].append(0)
    FenSurface['V3y'].append(-window_y1)
    FenSurface['V3z'].append(window_z1)
    FenSurface['V4x'].append(0)
    FenSurface['V4y'].append(-window_y1)
    FenSurface['V4z'].append(window_z2)

   ##### Shading ----------------------------------------------------
 
    if shading > 0:
 
        # Shading:Building:Detailed
 
        ShadingBuildingDetailed = {}
        ShadingBuildingDetailed['Name'] = []
        ShadingBuildingDetailed['Transmittance Schedule Name'] = []
        ShadingBuildingDetailed['Number of Vertices'] = []
        ShadingBuildingDetailed['V1x'] = []
        ShadingBuildingDetailed['V1y'] = []
        ShadingBuildingDetailed['V1z'] = []
        ShadingBuildingDetailed['V2x'] = []
        ShadingBuildingDetailed['V2y'] = []
        ShadingBuildingDetailed['V2z'] = []
        ShadingBuildingDetailed['V3x'] = []
        ShadingBuildingDetailed['V3y'] = []
        ShadingBuildingDetailed['V3z'] = []
        ShadingBuildingDetailed['V4x'] = []
        ShadingBuildingDetailed['V4y'] = []
        ShadingBuildingDetailed['V4z'] = []
 
        # Shading PZ1
        
        ShadingBuildingDetailed['Name'].append('Shading1')
        ShadingBuildingDetailed['Transmittance Schedule Name'].append('')
        ShadingBuildingDetailed['Number of Vertices'].append(4)
        ShadingBuildingDetailed['V1x'].append(0) 
        ShadingBuildingDetailed['V1y'].append(building_ylen+shading)
        ShadingBuildingDetailed['V1z'].append(ceiling_height+hpav)                            
        ShadingBuildingDetailed['V2x'].append(0)
        ShadingBuildingDetailed['V2y'].append(building_ylen)        
        ShadingBuildingDetailed['V2z'].append(ceiling_height+hpav)
        ShadingBuildingDetailed['V3x'].append(building_xlen)                    
        ShadingBuildingDetailed['V3y'].append(building_ylen)
        ShadingBuildingDetailed['V3z'].append(ceiling_height+hpav)
        ShadingBuildingDetailed['V4x'].append(building_xlen)
        ShadingBuildingDetailed['V4y'].append(building_ylen+shading)
        ShadingBuildingDetailed['V4z'].append(ceiling_height+hpav)
 
        # Shading PZ2
        
        ShadingBuildingDetailed['Name'].append('Shading2')
        ShadingBuildingDetailed['Transmittance Schedule Name'].append('')
        ShadingBuildingDetailed['Number of Vertices'].append(4)
        ShadingBuildingDetailed['V1x'].append(-shading) 
        ShadingBuildingDetailed['V1y'].append(0)
        ShadingBuildingDetailed['V1z'].append(ceiling_height+hpav)                            
        ShadingBuildingDetailed['V2x'].append(0)
        ShadingBuildingDetailed['V2y'].append(0)        
        ShadingBuildingDetailed['V2z'].append(ceiling_height+hpav)
        ShadingBuildingDetailed['V3x'].append(0)                    
        ShadingBuildingDetailed['V3y'].append(building_ylen)
        ShadingBuildingDetailed['V3z'].append(ceiling_height+hpav)
        ShadingBuildingDetailed['V4x'].append(-shading)
        ShadingBuildingDetailed['V4y'].append(building_ylen)
        ShadingBuildingDetailed['V4z'].append(ceiling_height+hpav)
 
        # Shading PZ3
        
        ShadingBuildingDetailed['Name'].append('Shading3')
        ShadingBuildingDetailed['Transmittance Schedule Name'].append('')
        ShadingBuildingDetailed['Number of Vertices'].append(4)
        ShadingBuildingDetailed['V1x'].append(building_xlen) 
        ShadingBuildingDetailed['V1y'].append(-shading)
        ShadingBuildingDetailed['V1z'].append(ceiling_height+hpav)                            
        ShadingBuildingDetailed['V2x'].append(building_xlen)
        ShadingBuildingDetailed['V2y'].append(0)        
        ShadingBuildingDetailed['V2z'].append(ceiling_height+hpav)
        ShadingBuildingDetailed['V3x'].append(0)                    
        ShadingBuildingDetailed['V3y'].append(0)
        ShadingBuildingDetailed['V3z'].append(ceiling_height+hpav)
        ShadingBuildingDetailed['V4x'].append(0)
        ShadingBuildingDetailed['V4y'].append(-shading)
        ShadingBuildingDetailed['V4z'].append(ceiling_height+hpav)
 
        # Shading PZ4
        
        ShadingBuildingDetailed['Name'].append('Shading4')
        ShadingBuildingDetailed['Transmittance Schedule Name'].append('')
        ShadingBuildingDetailed['Number of Vertices'].append(4)
        ShadingBuildingDetailed['V1x'].append(building_xlen+shading) 
        ShadingBuildingDetailed['V1y'].append(building_ylen)
        ShadingBuildingDetailed['V1z'].append(ceiling_height+hpav)                            
        ShadingBuildingDetailed['V2x'].append(building_xlen)
        ShadingBuildingDetailed['V2y'].append(building_ylen)        
        ShadingBuildingDetailed['V2z'].append(ceiling_height+hpav)
        ShadingBuildingDetailed['V3x'].append(building_xlen)                    
        ShadingBuildingDetailed['V3y'].append(0)
        ShadingBuildingDetailed['V3z'].append(ceiling_height+hpav)
        ShadingBuildingDetailed['V4x'].append(building_xlen+shading)
        ShadingBuildingDetailed['V4y'].append(0)
        ShadingBuildingDetailed['V4z'].append(ceiling_height+hpav)
        
    ####################------ ADD TO IDF ------####################
    
    # BuildingSurface:Detailed
    
    for i in range(len(BldgSurface['Name'])):
        obj = IDF._create_datadict("BuildingSurface:Detailed")
        obj['Name'] = BldgSurface['Name'][i]
        obj['Surface Type'] = BldgSurface['SurfaceType'][i]
        obj['Construction Name'] = BldgSurface['ConstructionName'][i]
        obj['Zone Name'] = BldgSurface['ZoneName'][i]
        obj['Outside Boundary Condition'] = BldgSurface['OutsideBoundaryCond'][i]
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

    #FenestrationSurface:Detailed
    
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
    
    # Shading:Building:Detailed
    if shading > 0:  
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

    # Zones
    
    for i in range(len(Zones['Name'])):
        obj = IDF._create_datadict('Zone')
        obj['Name'] = Zones['Name'][i]
        obj['Direction of Relative North'] = 0
        obj['Multiplier'] = 1
        obj['X Origin'] = Zones['X'][i]
        obj['Y Origin'] = Zones['Y'][i]
        obj['Z Origin'] = Zones['Z'][i] 
        idf.add(obj)

    # Building
    
    obj = IDF._create_datadict('Building')
    obj['Name'] = output #(str(ceiling_height)+'-'+str(building_xlen)+'-'+str(building_ratio)+'-'+str(wwr)+'-'+str(boundaries))
    
    obj['North Axis'] = azimuth
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
    
def sampleGen(file = 'sample.csv', path='C:\\Users\\Marcelo\\Documents\\'):
    
    os.chdir(path)
    condition = False
    i = 0
    
    dadoSample = pd.read_csv(file)
    with open(file,'r') as file_read:				
        lines = file_read.readlines()
    
    for line in lines:
        if condition == True:
            
            line = line.split(',')
            
            shell_depth = line[0]
            ceiling_height = line[1]
            building_xlen = line[2]
            building_ratio = line[3]
            wwr = line[4]
            boundaries = line[5]
            shading = line[6]
            hpav = line[7]
            azimuth = line[8]
            caso = '{:04.0f}'.format(i)
            output = ('caso_{}.idf'.format(caso))
            print(output)
            #print(shell_depth, ceiling_height,building_xlen, building_ratio, wwr, boundaries, shading, hpav, azimuth, output , path)
            out = main(shell_depth, ceiling_height,building_xlen, building_ratio, wwr, boundaries, shading, hpav, azimuth, output, path)
                      
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

sampleGen(path='C:/Users/Marcelo/gits/idf_generator')