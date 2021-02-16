#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:25:31 2020

@author: carlosdonosocabero

Transformaciones del dataset
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

wbr['casual_ratio']=(wbr.casual)/(wbr.registered)  #Creamos una columna nueva y le asignamos un valor
#Cuando creamos una variable nueva hay que hacerlo con [], no con el punto. Una vez ya esté creada entonces sí valen los dos métodos

wbr.casual_ratio.describe()
plt.hist(wbr.casual_ratio)

wbr.groupby(['workingday']).casual_ratio.describe()  #Segmento el dataset y le pido que haga los descriptivos sobre esa variable para cada tipo de workingday (2 veces)
#Observamos que las medias difieren entre día festivo (0) y laborable (1), hay dos grupos de días claramente diferenciados que se ven en el histograma

#Creo una nueva columna que transforme el contenido de la variable 'season' en strings
mytable=wbr.groupby(['season']).size()
print(mytable)

n= mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)

#Recoding 'season' into a string variable:
wbr.loc[ : , 'season_cat']= None  #Guardo en wbr en [x filas, y columnas] la palabra 'z', por ejemplo. Aquí es en todas las filas
#Caso concreto para una recodificación. Mejor no destruir nada y crear una nueva columna:
wbr= wbr.drop(columns='season_cat')  #Para borrar una columna
wbr.loc[(wbr['season']==1), 'season_cat']= 'Winter'
wbr.loc[(wbr['season']==2), 'season_cat']= 'Spring'
wbr.loc[(wbr['season']==3), 'season_cat']= 'Summer'
wbr.loc[(wbr['season']==4), 'season_cat']= 'Fall'

#QC: Vamos a hacer una tabulación cruzada para comprobar que está bien hecha la recodificación
pd.crosstab(wbr.season, wbr.season_cat)  #Es una tabla de doble entrada

wbr.loc[(wbr['season']==1), 'season_cat']= '1: Winter'
wbr.loc[(wbr['season']==2), 'season_cat']= '2: Spring'
wbr.loc[(wbr['season']==3), 'season_cat']= '3: Summer'
wbr.loc[(wbr['season']==4), 'season_cat']= '4: Fall'
pd.crosstab(wbr.season, wbr.season_cat)  #Para que salgan en la diagonal principal, aunque saldrán los nombres feos en el DataFrame

#Clasificar por rangos o clases

res = wbr.cnt.describe()
print(res)

m= res[1]
sd= res[2]
n= res[0]
c1= m-sd
c2= m+sd

wbr.loc[(wbr['cnt']<c1), 'cnt_cat2']= 'Low rentals'
wbr.loc[ (wbr['cnt']>=c1) & (wbr['cnt']<c2), 'cnt_cat2']= 'Average rentals'
wbr.loc[(wbr['cnt']>=c2), 'cnt_cat2']= 'High rentals'                 

#QC de la clasificación:
plt.scatter(wbr.cnt, wbr.cnt_cat2, s=1)
plt.axvline(x=m + sd, linewidth=1, linestyle='solid', color='green', label='+ SD')  #Pintamos rayitas en las +-SD
plt.axvline(x=m - sd, linewidth=1, linestyle='solid', color='red', label='- SD')

mytable= pd.crosstab(index= wbr['cnt_cat2'], columns= 'count')
print(mytable)
n= mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2)  #ERROR

wbr.info()  #Hay tres tipos de PANDAS datatypes: integers (enteros), floats (con decimales) y objects (texto/string; o mixed)

#####
from pandas.api.types import CategoricalDtype

my_categories=['Low rentals', 'Average rentals', 'High rentals']
my_rentals_type= CategoricalDtype(categories=my_categories, ordered=True)

wbr['cnt_cat7'] = wbr.cnt_cat2.astype(my_rentals_type)
plt.bar(wbr.cnt_cat7, wbr.cnt)  #Sale MAL el gráfico

