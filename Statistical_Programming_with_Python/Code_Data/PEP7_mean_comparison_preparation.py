# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:08:04 2019
@author: Alberto Sanz
Mean Comparison
MDA EDEM
"""
#Resets ALL (Careful This is a "magic" function then it doesn't run as script) 
#reset -f   

#load basiclibraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# New libraries
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import scipy.stats as stats  # For statistical inference 
import seaborn as sns  # For hi level, Pandas oriented, graphics

# Get working directory
os.getcwd()

# Change working directory
os.chdir('/Users/carlosdonosocabero/Desktop/MDA/PEP/CodeyData')
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
print(wbr.shape)
print(wbr.head())
print(wbr.info())
#QC OK

# Primero describimos las dos variables: wd y cnt de rentals

# Recode working day
# To string
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")
#To category
my_categories=["No", "Yes"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)
wbr.info()

#frequencies
mytable = pd.crosstab(index=wbr["wd_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Working Day')
plt.title('Figure 5. Percentage of Working Days')

######################
# Comparación de medias

wbr.groupby('wd_cat').cnt.mean()
#Los festivos vendo 4330 de media, y en laborables 4585

#Prueba de t: qué confianza tenemos para decir que hay asociación entre tipo de día y ventas
cnt_wd= wbr.loc[wbr.wd_cat=='Yes', 'cnt']
cnt_nwd= wbr.loc[wbr.wd_cat=='No', 'cnt']

import scipy.stats as stats  #Esto se tendrá que poner siempre arriba junto con el resto de librerías

stats.ttest_ind(cnt_wd, cnt_nwd, equal_var= False)
# Hazme una prueba de t para comparar las dos medias de los dos grupos, y no asumas nada (sé lo más conservador posible), por eso False
# P.value mide el riesgo de equivocarnos al rechazar Ho, por eso queremos pvalue<0.05, al menos

#Comparación gráfica: intervalos de confianza para las medias
import seaborn as sns
import matplotlib.pyplot as plt  #Esto se tendrá que poner siempre arriba junto con el resto de librerías

ax = sns.pointplot(x="wd_cat", y="cnt", data=wbr, ci=95, join=0)
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(0.85,5400,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110', bbox=props)
plt.xlabel('Working Day')
plt.title('Figure 6. Average rentals by Working Day.''\n')

# Otro ejemplo
wbr.groupby('yr').cnt.mean()
#Aquí el tamaño del efecto es mayor, ya pinta mejor

cnt_2011= wbr.loc[wbr.yr==0, 'cnt']
cnt_2012= wbr.loc[wbr.yr==1, 'cnt']

#Prueba de t
stats.ttest_ind(cnt_2011, cnt_2012, equal_var= False)  # Ahora sí rechazamos la Ho

#Gráficamente se ve claro
ax = sns.pointplot(x='yr', y="cnt", data=wbr, ci=99, join=0)
plt.yticks(np.arange(3000, 6500, step=500))
plt.ylim(2800,6200)
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(-0.3,5400,'Mean:4504.3''\n''n:731' '\n' 't:-18.58' '\n' 'Pval.:1.05e-62', bbox=props)
plt.xlabel('Year')
plt.xticks((0,1), ('2011','2012'))
plt.title('Figure 7. Average rentals by Year.''\n')


#Comparación con 3 grupos: ANOVA

#Recode weather situation
#To string
wbr["ws_st"] = wbr.weathersit
wbr.ws_st = wbr.ws_st.replace(to_replace=1, value="Sunny")
wbr.ws_st = wbr.ws_st.replace(to_replace=2, value="Cloudy")
wbr.ws_st = wbr.ws_st.replace(to_replace=3, value="Stormy")
#To category
my_categories=["Sunny", "Cloudy", "Stormy"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["ws_cat"] = wbr.ws_st.astype(my_datatype)
wbr.info()
#Frequencies
mytable = pd.crosstab(index=wbr["ws_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Weather Situation')
plt.title('Figure 8. Percentage of Weather Situation')

#Describimos
wbr.groupby('ws_cat').cnt.mean()

cnt_sunny=wbr.loc[wbr.ws_cat=='Sunny', "cnt"]
cnt_cloudy=wbr.loc[wbr.ws_cat=='Cloudy', "cnt"]
cnt_stormy=wbr.loc[wbr.ws_cat=='Stormy', "cnt"]

#One-Way ANOVA
stats.f_oneway(cnt_sunny, cnt_cloudy, cnt_stormy)  #Rechazamos Ho: al menos 2 grupos difieren

#Gráficamente
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="ws_cat", y="cnt", data=wbr, capsize=0.05, ci=99.9, join=0)
ax.set_ylabel('')
plt.yticks(np.arange(1000, 7000, step=500))
plt.ylim(800,6200)
plt.axhline(y=wbr.cnt.mean(), linewidth=1, linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5) 
plt.text(1.5, 5000, 'Mean: 4504.3''\n''n: 731' '\n' 'F: 40.06' '\n' 'Pval.: 0.000', bbox=props)
plt.xlabel('Weather Situation')
plt.title('Figure 9. Average rentals by Weather Situation.''\n')
