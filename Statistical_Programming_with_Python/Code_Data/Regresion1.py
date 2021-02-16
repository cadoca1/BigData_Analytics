#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:03:07 2020

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

model1a = ols('cnt ~ temp_celsius', data=wbr).fit()  #Primero y, luego x aquí
model1a.summary2()

model1b = ols('cnt ~ windspeed_kh', data=wbr).fit()
model1b.summary2()  #Es significativa también y negativa, pero R2 es mucho menor: solo el 6% depende de la variabilidad en el viento

###

model2 = ols('cnt ~ temp_celsius + windspeed_kh', data=wbr).fit()  #Dos predictores ahora
model2.summary2()

###

wbr.hum.hist()  #Describir primero SIEMPRE
model1c= ols('cnt ~ hum', data=wbr).fit()
model1c.summary2()

model3= ols('cnt ~ temp_celsius + windspeed_kh + hum', data=wbr).fit()
model3.summary2()  #Aumenta R2 respecto a model2 y cambian los coeficientes

### Para reportar

#!pip install stargazer
from stargazer.stargazer import Stargazer

stargazer= Stargazer([model1a, model2, model3])
stargazer.render_html()
