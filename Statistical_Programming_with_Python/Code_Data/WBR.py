#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:51:03 2020

@author: carlosdonosocabero

Dibujar
"""

#%reset -f

import os  #sistema operativo
import pandas as pd  #le llama así a pandas, que sirve para gestionar matrices de datos desde Python
import numpy as np  #operaciones numéricas
import matplotlib.pyplot as plt  #gráficas

os.chdir('/Users/carlosdonosocabero/Desktop/MDA/PEP/CodeyData')
os.getcwd()

wbr=pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')

wbr.shape
#QC OK

#Quiero describir la variable cuantitativa número de alquileres o cnt (count)

wbr.cnt.mean()  #La media
wbr.cnt.min()  #El mínimo
wbr.cnt.describe()  #Hace todos los descriptivos

res = wbr.cnt.describe()  #Guardo en un nuevo objeto los resultados descriptivos
res[0]  #Para acceder a cada uno
res[1]


#Hacer gráficos plot
x=wbr.cnt
x=wbr['cnt']  #Es lo mismo que lo anterior

plt.hist(x)
plt.hist(x, edgecolor='black')

ticks=np.arange(0,10000,1000)  #No llega a 10000 y va de 1000 en 1000
plt.xticks(ticks)

plt.hist(x, edgecolor='black')
plt.xticks(ticks)
plt.show()  #Es cerrarlo, como imprimirlo, lo siguiente que se añada de plots se generará sobre un gráfico nuevo

plt.hist(x, bins=2, edgecolor='black', color='white')  #bins es cuántos bloques o barras habrá en el histograma

plt.hist(x, bins=10, edgecolor='black')
plt.xticks(ticks)
plt.title('Figure 1' '\n' 'separo lineas')
plt.ylabel('Frequency')
plt.xlabel('Bicycles rented')
plt.show()

m= res[1]
sd= res[2]
n= res[0]
print(round(res[1],1))

plt.hist(x)
plt.text(6000,100,'Hola')  #Añadir texto en las coordenadas x,y que diga

plt.hist(x, bins=10, edgecolor='black')
plt.xticks(ticks)
plt.title('Figure 1' '\n' 'separo lineas')  #Usar el \n para hacer salto de línea
plt.ylabel('Frequency')
plt.xlabel('Bicycles rented')
textstr= 'Mean = 4504\nSD = 1937 \nn = 731'
plt.text(6500,110,textstr)  #También se podría poner directamente la str ahí en vez del objeto
plt.axvline(x=m, linewidth=1, linestyle='solid', color='red', label='Mean')  #Poner línea roja indicando la media
plt.show()

#Así, ponemos en un recuadro los datos de texto:
plt.hist(x, bins=10, edgecolor='black')
plt.xticks(ticks)
plt.title('Figure 1' '\n' 'separo lineas')  #Usar el \n para hacer salto de línea
plt.ylabel('Frequency')
plt.xlabel('Bicycles rented')
props = dict(boxstyle='round', facecolor='white', lw= 0.5)
textstr = '$\mathrm{Mean}=%.1f$\n$\mathrm{S.D.}=%.1f$\n$\mathrm{n}=%.0f$'%(m, sd, n) 
plt.text (6500,110, textstr, bbox=props)
plt.axvline(x=m, linewidth=3, linestyle='solid', color='orange', label='Mean')  #Poner línea roja indicando la media
plt.show()


#Describir una variable cualitativa, como weather situation

mytable=wbr.groupby(['weathersit']).size()
print(mytable)  #Frecuencias absolutas

n= mytable.sum()

mytable2=(mytable/n)*100

mytable3=round(mytable2,1)
print(mytable3)

#Barchart
plt.bar(mytable2.index,mytable2)  #Utilizo mytable2 donde ya tengo los % de cada uno

bar_list=['Sunny', 'Cloudy', 'Rainy']

plt.bar(bar_list,mytable2)
plt.title('Figure 2')
plt.ylabel('%')
plt.xlabel('Weather Situation')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n) 
plt.text(2, 60, textstr, bbox=props)  #Para poner n en un recuadro como texto

