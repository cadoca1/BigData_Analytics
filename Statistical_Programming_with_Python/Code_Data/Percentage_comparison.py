# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:08:04 2019
@author: Alberto Sanz
Percentage Comparison
MDA EDEM

"""
#Resets ALL (Careful This is a "magic" function then it doesn't run as script) 
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

#Recoding DV for analysis
res = wbr.cnt.describe()
print (res)
# Store parameters as numbers
m  = res[1]
sd = res[2]
n  = res[0]

### Recode cnt to string
wbr.loc[  (wbr['cnt']<(m-sd)) ,"cnt_str"]= "Low rentals"
wbr.loc[ ((wbr['cnt']>=(m-sd)) & (wbr['cnt']<(m+sd))) ,"cnt_str"]= "Average rentals"
wbr.loc[  (wbr['cnt']>=(m+sd)) ,"cnt_str"]= "High rentals"

### Recode cnt_str to ordinal/categorical
my_categories=["Low rentals", "Average rentals", "High rentals"]
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True)
wbr["cnt_cat"] = wbr.cnt_str.astype(my_rentals_type)
wbr.info()

#frequencies & barchart
mytable = pd.crosstab(wbr.cnt_cat, columns="count", normalize='columns')*100
print(mytable)
print (round(mytable,1))
plt.bar(mytable.index, mytable['count'])
plt.show()

#######################
# Recode working day
# To string
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")
#To category
my_categories=["No","Yes"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)
wbr.info()

# Barchart for Working day
mytable = pd.crosstab(index=wbr["wd_cat"], columns="count") # Crosstab
n=mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
plt.bar(mytable2.index, mytable2['count'])
plt.xlabel('Working Day')
plt.title('Figure 5. Percentage of Working Days')

#########################

#Tablas de contingencia: SIEMPRE primero la dependiente y luego la independiente
pd.crosstab(wbr.cnt_cat, wbr.wd_cat, margins=True)  #margins=True es para que ponga una columna con el total
#Pero lo queremos en % por columnas (no por filas)
pd.crosstab(wbr.cnt_cat, wbr.wd_cat, normalize='columns', margins=True)*100
#Para saber si QC OK miro en la total si sigue la distribución porcentual de la variable dependiente (20x60x20)

my_ct= pd.crosstab(wbr.cnt_cat, wbr.wd_cat, normalize='columns', margins=True)*100

round(my_ct,1)  #Aplico una función (algo externo que ataca a unos datos)
my_ct.round(1)  #A partir de un objeto aplico un método

ct= pd.crosstab(wbr.cnt_cat, wbr.wd_cat)  #¡¡¡Sin el total y sin pedir normalizar por columnas (sin %)!!!
stats.chi2_contingency(ct)
#El primer valor es el estadístico y el segundo es el p-value, el cual no es menor a 0.05, por lo que no rechazamos Ho

#Gráficamente: representamos los % (my_ct), a nadie le importan las frecuencias
my_ct.plot(kind="bar")  #No queremos esto
my_ct2= my_ct.transpose()  #Trasponemos la tabla de contingencia para darle la vuelta al gráfico

my_ct2.plot(kind="bar", edgecolor = "black", colormap='Blues')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(-0.4, 81, 'Chi2: 4.98''\n''n: 731' '\n' 'Pval.: 0.083', bbox=props)
plt.xlabel('Working Day')
plt.title('Figure 7. Percentage of Rental level, by Working Day.''\n')
plt.legend(['Low rentals','Average rentals','High rentals'])
plt.ylim(0,100)  #Para poner límite inferior y superior del eje y
plt.xticks(rotation='horizontal')  #Para girar los nombres de las x
plt.show()

#Ahora lo mismo pero con la WEATHER SITUATION

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

#Tabla de contingencia
pd.crosstab(wbr.cnt_cat, wbr.ws_cat, margins=True)
pd.crosstab(wbr.cnt_cat, wbr.ws_cat, normalize='columns', margins=True)*100

#Estadístico Chi-2
ct_ws= pd.crosstab(wbr.cnt_cat, wbr.ws_cat)
stats.chi2_contingency(ct_ws)  #Aquí sí rechazamos Ho

#Gráficamente
ct_ws_1= pd.crosstab(wbr.cnt_cat, wbr.ws_cat, normalize='columns', margins=True)*100
ct_ws_2= ct_ws_1.transpose()

ct_ws_2.plot(kind="bar", edgecolor = "black", colormap='Blues')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(-0.4, 81, 'Chi2: 68.77''\n''n: 731' '\n' 'Pval.: 0.000', bbox=props)
plt.xlabel('Weather Situation')
plt.title('Figure 8. Percentage of Rental level, by Weather Situation.''\n')
plt.legend(['Low rentals','Average rentals','High rentals'])
plt.ylim(0,100)
plt.xticks(rotation='horizontal')

#####################
#Para guardar la sesión y que el entorno vuelva a ser el mismo cuando reinicies

#!pip install dill  #Para coger librería de fuera de Anaconda
import dill

filename= '/Users/carlosdonosocabero/Desktop/MDA/PEP/CodeyData/Percentage_comparison.py'
dill.dump_session(filename)  #Guardar

dill.load_session(filename)  #Cargar

#También se puede hacer manualmente mediante ventanitas

