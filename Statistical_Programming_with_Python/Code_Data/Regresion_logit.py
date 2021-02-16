# -*- coding: utf-8 -*-
"""
Spyder Editor

Regresión logística
"""

#%reset -f

import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference

os.getcwd()
os.chdir("/Users/carlosdonosocabero/Desktop/MDA/PEP/CodeyData")

wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
wbr.shape
wbr.head()
#QC OK

from statsmodels.formula.api import ols

model1 = ols('cnt ~ temp_celsius', data=wbr).fit()
print(model1.summary2())

model2 = ols('cnt ~ windspeed_kh', data=wbr).fit()
print(model2.summary2())

model3 = ols('cnt ~ temp_celsius + windspeed_kh', data=wbr).fit()
print(model3.summary2())
#El coeficiente es menor, es menos fuerte, cuando controlas por el impacto de las demás (temp), porque antes estaba absorbiendo el efecto de la temp, y ahora es ceteris paribus

wbr['temp_2'] = wbr.temp_celsius**2  #Para elevar se puede hacer así

model4 = ols('cnt ~ temp_celsius + temp_2 + windspeed_kh', data=wbr).fit()
print(model4.summary2())

model5 = ols('cnt ~ temp_celsius + windspeed_kh + yr', data=wbr).fit()
print(model5.summary2())

# One-Hot Encoding: para variables dummies cualitativas de más de dos estados. Se expanden en tantas columnas como estados haya, pero dejando fuera una categoría de referencia
dummies = pd.get_dummies(wbr.weathersit)
colnames = {1:'sunny', 2:'cloudy', 3:'rainy'}
dummies.rename(columns=colnames, inplace=True)
wbr = pd.concat([wbr,dummies], axis=1)
#Siempre hacer QC con un crosstab de las nuevas con el antiguo

model6 = ols('cnt ~ temp_celsius + windspeed_kh + cloudy + rainy', data=wbr).fit()
print(model6.summary2())

""""
Regresión logística

""""

wbr.cnt.describe()
wbr.cnt.hist()
m = wbr.cnt.mean()
wbr.loc[(wbr['cnt'] <= m), 'goal'] = 0
wbr.loc[(wbr['cnt'] > m), 'goal'] = 1

pd.crosstab(wbr.cnt, wbr.goal)
plt.scatter(wbr.cnt, wbr.goal)

from statsmodels.formula.api import logit

model_l1 = logit('goal ~ temp_celsius', data=wbr).fit()
print(model_l1.summary2())  #Haremos caso al Pseudo R-squared

model_l2 = logit('goal ~ temp_celsius + temp_2', data=wbr).fit()
print(model_l2.summary2())

model_l3 = logit('goal ~ temp_celsius + temp_2 + windspeed_kh', data=wbr).fit()
print(model_l3.summary2())  #Va mejorando el modelo pero sigue siendo baja la pseudo R2


