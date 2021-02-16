#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:00:54 2020

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

from statsmodels.formula.api import ols

model1a = ols('cnt ~ temp_celsius', data=wbr).fit()
model1a.summary2()  #El p-value es significativo, la temperatura es importante para explicar las ventas

model2 = ols('cnt ~ temp_celsius + windspeed_kh', data=wbr).fit()
model2.summary2()

model3= ols('cnt ~ temp_celsius + windspeed_kh + hum', data=wbr).fit()
model3.summary2()

model1d= ols('cnt ~ workingday', data=wbr).fit()
model1d.summary2() #Cuando paso de 0 a 1 las ventas se incrementan en 255 uds.; y en 0 (festivos), venderé 4330. Es decir, en laborables venderé 4585

model4= ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday', data=wbr).fit()
model4.summary2() #wkd no es significativa, incluso baja aquí más aun la significatividad al controlar por otras variables

model5= ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday + yr', data=wbr).fit()
model5.summary2()  #yr sí es significativa y R2 ha subido mucho
#La media de las ventas de un año a otro subió en 2007 uds., ceteris paribus y con el resto de coeficientes = 0
#Por tanto, ceteris paribus, en 2011 se venden 2515 y en 2012, 4522 (resto coeficientes = 0)

dummies= pd.get_dummies(wbr.weathersit)  #Para obtener las 3 columnas con las dummies (0 es ausencia de la característica y 1 es lo contrario)

colnames= {1:'sunny', 2:'cloudy', 3:'rainy'}  #Es un diccionario
dummies.rename(columns= colnames, inplace= True) #Rename column labels inplace (en el mismo df, no crea uno nuevo)

wbr_dummies= pd.concat([wbr,dummies], axis=1)
#Sin esto habría que haber hecho una recodificación (loc)

pd.crosstab(wbr_dummies.weathersit, wbr_dummies.sunny)
#QC OK

wbr= pd.concat([wbr,dummies], axis=1)  #Ahora que ya se que está bien, antes no para no cargármelo

model6a= ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday + yr + cloudy + rainy', data=wbr).fit()
model6a.summary2() #Hay que dejar una fuera que sirva como referencia (sunny); si es cloudy venderemos 477 menos con respecto a sunny; y si es rainy pues -1787
#Es siempre respecto a la referente, que será normalmente la que sea más común
#Si es sunny, ceteris paribus, venderé 1721

model6b= ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday + yr + sunny + cloudy', data=wbr).fit()
model6b.summary2()

#Ahora con season
dummies2= pd.get_dummies(wbr.season)
colnames2= {1:'winter', 2:'spring', 3:'summer', 4:'fall'}
dummies2.rename(columns= colnames2, inplace= True)
wbr= pd.concat([wbr,dummies2], axis=1)
model7= ols('cnt ~ temp_celsius + windspeed_kh + hum + workingday + yr + cloudy + rainy + winter + spring + fall', data=wbr).fit()
model7.summary2()  #Sacamos un extremo, verano por ejemplo, para la nueva variable dummy 'season'
#Aquí sin tener en cuenta las nuevas variables de este modelo, controlando por esas variables, ya tiene importancia workingday
#Nota: Si salen dobles es porque he concatenado sobre la anterior que ya estaba concatenada

#################

#Dealing with non-linear relations

wbr['temp2']= wbr.temp_celsius * wbr.temp_celsius  #El cuadrado de la temperatura, porque creo que es una relación cuadrática mirando el scatter plot, para linealizarla

model8= ols('cnt ~ temp_celsius + temp2 + windspeed_kh + hum + workingday + yr + cloudy + rainy + winter + spring + fall', data=wbr).fit()
model8.summary2()

