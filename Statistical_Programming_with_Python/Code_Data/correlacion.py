#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:17:46 2020

@author: carlosdonosocabero
"""

#%reset -f   

#load basiclibraries
import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 

os.chdir('/Users/carlosdonosocabero/Desktop/MDA/PEP/CodeyData')
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
wbr.shape
wbr.head()
#QC OK

#Vamos a buscar correlación de cnt con temperatura (dos variables cuantitativas)

#Primero hay que describir las dos variables, como siempre hemos hecho antes de cualquier otra cosa

#La de cnt ya la hicimos, ahora hacemos la de temperatura
temp= wbr.temp_celsius
temp.describe()
plt.hist(temp)
#Mucha dispersión, dos modas, o hace mucho frío o mucho calor, muy polarizada, alta sd. No sigue una distribución normal (como sí pasa con cnt)

x= wbr.temp_celsius
y= wbr.cnt

plt.scatter(wbr.temp_celsius, wbr.cnt)  #Primero 'x' (independiente) y luego 'y' (dependiente)

plt.figure(figsize=(5,5))
plt.scatter(x, y, s=20, facecolor='none', edgecolor='C0')  #Para hacer los puntos huecos y azules
#plt.xticks(np.arange(0,11,1))
plt.yticks(np.arange(0,10000,1000))
textstr= 'r = 0.63\np-value = 0.000 \nn = 731'
props = dict(boxstyle='round', facecolor='white', lw= 0.5)
plt.text(4,7500,textstr, bbox=props)
plt.title('Figure 9. Daily bicycle rentals, by temperature' '\n')
plt.ylabel('Daily rentals')
plt.xlabel('Temperature')
plt.show()
#Se ve una relación directa (no inversa): a más temp más ventas; fuerte; y positiva

wind_speed=wbr.windspeed_kh
wind_speed.describe()
plt.hist(wind_speed)

plt.figure(figsize=(5,5))
plt.scatter(wbr.windspeed_kh, wbr.cnt, s=20, facecolor='none', edgecolor='C0')
#plt.xticks(np.arange(0,11,1))
plt.yticks(np.arange(0,10000,1000))
textstr= 'r = -0.23\np-value = 0.000 \nn = 731'
props = dict(boxstyle='round', facecolor='white', lw= 0.5)
plt.text(24,7700,textstr, bbox=props)
plt.title('Figure 10. Daily bicycle rentals, by wind speed' '\n')
plt.ylabel('Daily rentals')
plt.xlabel('Wind speed')
plt.show()
#Aquí hay relación inversa, pero es menos fuerte que antes

from scipy.stats import pearsonr

pearsonr(wbr.temp_celsius, wbr.cnt)
pearsonr(x,y)  #Lo mismo
#El primero es el coeficiente de correlación de Pearson; el segundo, el p-value

pearsonr(wbr.windspeed_kh, wbr.cnt)
#Aquí efectivamente la correlación es menos fuerte

n= len(wbr.cnt) ##

plt.figure(figsize=(5,5))
plt.scatter('temp_celsius', 'cnt', data=wbr, c='yr') #En efecto, era el año
plt.scatter(x,y,c=wbr.yr)  #Otra forma

#Veamos por season
plt.figure(figsize=(5,5))
plt.scatter('temp_celsius', 'cnt', data=wbr, c='season')
#Season no aporta valor aquí, porque es una ordinal de la temperatura, que era mejor

#Hacemos sub-setting por año
plt.figure(figsize=(5,5))
plt.scatter(wbr.temp_celsius[wbr.yr==0], wbr.cnt[wbr.yr==0], s=20, marker='s', facecolor='none', edgecolor='C0', label='2011')  #Marker es un marcador (buscar en Google)
#plt.legend()  #Aunque aquí no tiene sentido, porque solo hay un año
plt.scatter(wbr.temp_celsius[wbr.yr==1], wbr.cnt[wbr.yr==1], s=20, facecolor='none', edgecolor='C1', label='2012')
plt.legend(loc='upper right')
textstr= 'r = 0.63\np-value = 0.000\nn = 731'
props = dict(boxstyle='round', facecolor='white', lw= 0.5)
plt.text(4,7700,textstr, bbox=props)
plt.title('Figure 11. Daily bicycle rentals, by temperature and year' '\n')  #Usar el \n para hacer salto de línea
plt.ylabel('Daily rentals')
plt.xlabel('Temperature')
plt.savefig('delfines.svg')  #Lo bueno es que es vectorial y lo dibuja mejor (el jpg pierde calidad porque no sabe lo que tiene dentro)
plt.savefig('delfines.jpg')  #Guarda en el working directory
plt.show()

