#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:03:51 2020

@author: carlosdonosocabero
"""

#%reset -f

import os  #sistema operativo
import pandas as pd  #le llama así a pandas, que sirve para gestionar matrices de datos desde Python
import numpy as np  #operaciones numéricas
import matplotlib.pyplot as plt  #gráficas

os.getcwd()
os.chdir('/Users/carlosdonosocabero/Desktop/MDA/PEP/CodeyData')
rentals_2011= pd.read_csv ('washington_bike_rentals_2011.csv', sep=';', decimal=',')  #Importante para diferenciar csv europeo de americano

#Para comprobar si ha habido errores, que siempre estarían o al principio o al final
rentals_2011.shape
rentals_2011.head()  #Incluir paréntesis
rentals_2011.tail()

#Select the variable to plot
rentals_2011.cnt  #Variable del recuento de número de alquileres en cada día

plt.hist(rentals_2011.cnt)  #Para dibujar el histograma de esa variable
plt.hist(rentals_2011.casual)
plt.hist(rentals_2011.registered)

plt.hist(rentals_2011.cnt, edgecolor='black')
plt.xticks(np.arange(0, 7000, step=1000))  #Hay que poner el final en uno más que donde quiero que acabe (contrario que R e intuición)
plt.title('Figure 1. Registered rentals in Washington')
plt.show()  #Es para parar la gráfica

x=rentals_2011.cnt
y=rentals_2011.casual

plt.hist(x, edgecolor='black')
plt.xticks(np.arange(0, 7000, step=1000))  #Hay que poner el final en uno más que donde quiero que acabe (contrario que R e intuición)
plt.title('Figure 1. Registered rentals in Washington')
plt.show()  #Si no pones esto en medio te saldrán las dos gráficas solapadas
plt.hist(y, edgecolor='black')

del(x,y)

##################
weather_2011= pd.read_csv ('weather_washington_2011.csv', sep=';', decimal=',')

weather_2011.shape
weather_2011.head()
weather_2011.tail()
#QC OK

rentals_weather_2011= pd.merge(weather_2011, rentals_2011, on='day')  #On es la clave que los une (o merge)

rentals_weather_2011.shape
rentals_weather_2011.head()
rentals_weather_2011.tail()

#QC OK? No, hay una variable duplicada, la de fecha, porque era común

rentals_weather_2011=rentals_weather_2011.drop(columns=['dteday_y'])  #Drop es quitar y se usan esos corchetes

rentals_weather_2011=rentals_weather_2011.rename(columns={'dteday_x': 'dteday'})  #Se utilizan esas llaves porque es un diccionario, una equivalencia

rentals_weather_2011.shape
print(rentals_weather_2011.head())

plt.scatter(rentals_weather_2011.temp_celsius,rentals_weather_2011.cnt)  #Primero la x y luego la y

####################

#Vamos a añadir ahora filas o casos, no columnas, un DataFrame del 2012 y haremos un merge de los dos grandes (2011 y 2012) para crear un nuevo DataFrame

rentals_weather_2012= pd.read_csv('rentals_weather_2012.csv', sep=';', decimal=',')

rentals_weather_2012.shape  #Año bisiesto, no hay problema, mientras las columnas sean las mismas no hay problema con que las filas difieran
rentals_weather_2011.shape

rentals_weather_2012.head()
#QC OK

rentals_weather_11_12= rentals_weather_2011.append(rentals_weather_2012)  #Añadir por debajo (más filas) es "append"; añadir al lado (más columnas) es "merge"

rentals_weather_11_12.shape
rentals_weather_11_12.head()
rentals_weather_11_12.tail()
#QC OK

rentals_weather_11_12= rentals_weather_2011.append(rentals_weather_2012, ignore_index= True)  #Ignorar la columna de index al importar el DataFrame de 2012 por debajo para que no lo copie tal cual y llegue hasta 730


rentals_weather_11_12= rentals_weather_11_12[rentals_weather_2011.columns]  #Para cambiar orden de columnas según el orden del de 2011, se puede eso o poner cualquier otro orden creando una lista cualquiera con el orden deseado
rentals_weather_2011.columns
orden= rentals_weather_2011.columns
rentals_weather_11_12= rentals_weather_11_12[orden]

orden2=['weathersit', 'day', 'dteday', 'temp_celsius', 'windspeed_kh', 'atemp', 'hum', 'season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'casual', 'registered', 'cnt']
rentals_weather_11_12= rentals_weather_11_12[orden2]

rentals_weather_11_12.to_csv('rentals_weather_11_12.csv')
