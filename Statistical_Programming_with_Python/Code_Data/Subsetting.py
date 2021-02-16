#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:07:57 2020

@author: carlosdonosocabero
"""

"""
Para escribir un texto largo.
Con varios párrafos
"""
#%reset -f

import os  #sistema operativo
import pandas as pd  #le llama así a pandas, que sirve para gestionar matrices de datos desde Python
import numpy as np  #operaciones numéricas
import matplotlib.pyplot as plt  #gráficas

os.chdir('/Users/carlosdonosocabero/Desktop/MDA/PEP/CodeyData')
os.getcwd()

wbr=pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')

plt.hist(wbr.cnt)

#Quiero hacer dos DataFrames (uno para cada año) a partir de uno previo
mytable=wbr.groupby(['yr']).size()
print(mytable)

#Porcentajes
n= mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)  #Donde 0 es 2011 y 1 es 2012

wbr_2011= wbr[wbr.yr==0]  #Atención poner doble = para hacer una comparación, sino estaría asignando un valor a un objeto
wbr_2012= wbr[wbr.yr==1]
#Ya tenemos el sub-setting, por años en este caso

plt.hist(wbr_2011.cnt)
plt.hist(wbr_2012.cnt)

wbr_2011.cnt.describe()
wbr_2012.cnt.describe()

wbr_2012_winter= wbr[(wbr.yr==1)&(wbr.season==1)]
wbr_2012_winter.shape
plt.hist(wbr_2012_winter.cnt)
wbr_2012_winter.cnt.describe()
#Esto se puede hacer de otra forma tb (en 2 pasos), partiendo de wbr_2012 en vez de wbr

wbr_winter_fall= wbr[(wbr.season==1)|(wbr.season==4)]
wbr_winter_fall.shape
###
mytable2=wbr_winter_fall.groupby(['season']).size()
print(mytable2)
#QC OK

wbr_winter_fall.cnt.hist()
plt.hist(wbr_winter_fall.cnt)  #Las dos formas es lo mismo, la primera con objetos y la segunda con una función o mediante métodos
