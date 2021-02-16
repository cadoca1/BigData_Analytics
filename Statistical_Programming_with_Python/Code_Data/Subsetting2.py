#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:48:26 2020

@author: carlosdonosocabero
"""

#%reset -f

import os  #sistema operativo
import pandas as pd  #le llama así a pandas, que sirve para gestionar matrices de datos desde Python
import numpy as np  #operaciones numéricas
import matplotlib.pyplot as plt  #gráficas

os.chdir('/Users/carlosdonosocabero/Desktop/MDA/PEP/CodeyData')
os.getcwd()

wbr_ue=pd.read_csv('wbr_ue.csv', sep=';', decimal=',')
wbr_ue.head()

#Sub-setting por columnas
my_vars=['temp_celsius', 'cnt']

wbr_minimal= wbr_ue[my_vars]  #Contiene todos los casos pero con solo dos columnas
wbr_minimal.shape

wbr_ue.temp_celsius.describe()
plt.hist(wbr_ue.temp_celsius)  #Está mal así, siempre plot your data para asegurar

#Limpiamos el dataset
wbr_ue['temp_celsius_c']= wbr_ue.temp_celsius.replace(99,np.nan)  #Digo que los 99 son nan (not a number), reemplazo los 99 por nan, por huecos
wbr_ue.temp_celsius_c.describe()  #Ahora bien
plt.hist(wbr_ue.temp_celsius_c)  #Pero esto puede no funcionar debido a los nan
plt.boxplot(wbr_ue.temp_celsius_c)  #De hecho, este no funciona

wbr_ue.temp_celsius_c.dropna()  #Esto es muy importante para quitar los na y que se pueda hacer el histograma, aunque aquí no ha habido problema para que se dibuje
plt.hist(wbr_ue.temp_celsius_c.dropna())
plt.boxplot(wbr_ue.temp_celsius_c.dropna())  #Así sí

wbr_ue2=wbr_ue.dropna()  #Para limpiar todo el dataset de nas, no solo de una columna
print(wbr_ue2.shape)
print(wbr_ue.shape)  #Hay un caso de más (732), porque debería ser 731, seguramente sea una duplicidad y hay que encontrarla y eliminarla

#Conclusión: ALWAYS PLOT YOUR DATA!!!

#Para eliminar duplicados:
wbr_ue.duplicated()  #Para cada caso, nos dice si está duplicado o no
wbr_ue[wbr_ue.duplicated(keep=False)]
#Las filas 396 y 397 están duplicadas
wbr_ue_nuevo= wbr_ue.drop([397],axis=0)  #Borramos la 397

#Otra forma más FÁCIL y directa:
wbr_ue_nuevo2= wbr_ue.drop_duplicates('instant', keep= 'last')

