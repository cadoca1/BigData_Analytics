#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:06:53 2020

@author: carlosdonosocabero
"""

#%reset -f

import os  #sistema operativo
import pandas as pd  #le llama así a pandas, que sirve para gestionar matrices de datos desde Python
import numpy as np  #operaciones numéricas
import matplotlib.pyplot as plt  #gráficas

os.getcwd()
os.chdir('/Users/carlosdonosocabero/Desktop/MDA/PEP/CodeyData')

youtube= pd.read_csv('USvideos.csv', sep=',', decimal='.')

youtube.shape
youtube.head()
youtube.tail()
#QC OK

#Describimos numéricamente la variable cuantitativa 'views'
views= youtube.views
views_describe= views.describe()
v_n= views_describe[0]
v_m= views_describe[1]
v_sd= views_describe[2]  #Es muy alta, el triple que la media 
print(views_describe)
print(v_n)
print(round(v_m,0))
print(round(v_sd,0))

#Describimos gráficamente la variable cuantitativa 'views'
plt.hist(views)
plt.show()
#Hay tanta dispersión que la escala hace que en la gráfica todos los valores se vean concentrados
print(views_describe)
print(views.max())

#Por tanto, analizamos aquellos vídeos que tienen un número de visualizaciones < 2.000.000
views_nuevo= views[views<2000000]
views_nuevo
views_nuevo_describe= views_nuevo.describe()
v2_n= views_nuevo_describe[0]
v2_m= views_nuevo_describe[1]
v2_sd= views_nuevo_describe[2]

plt.hist(views_nuevo/1000000, bins=10, edgecolor='black')
ticks= np.arange(0,2.2,0.2)
plt.xticks(ticks)
plt.title('Figura 1. Visualizaciones en vídeos de YouTube.''\n')
plt.ylabel('Número de vídeos')
plt.xlabel('Millones de visualizaciones')
textstr= 'Media = 593.841\nSD = 516.289\nn = 31.523'
props = dict(boxstyle='round', facecolor='white', lw= 0.5)
plt.text(1.4,7000,textstr, bbox=props)
plt.axvline(x=v2_m/1000000, linewidth=1, linestyle='solid', color='red', label='Media')
plt.axvline(x=(v2_m+v2_sd)/1000000, linewidth=1.5, linestyle='dashed', color='green', label='+SD')
plt.axvline(x=(v2_m-v2_sd)/1000000, linewidth=1.5, linestyle='dashed', color='green', label='-SD')
plt.show()

######
plt.scatter(views, youtube.likes)  #Correlación positiva, pero decreciente marginalmente (función logarítmica)
plt.scatter(views, youtube.dislikes)
plt.show()
######

#Calculamos los porcentajes
mytable=youtube.groupby(['category_id']).size()
print(mytable)
n= mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)
mytable2.sum()  #QC OK
mytable3= round(mytable2,1)
print(mytable3)

#Creamos nueva columna cualitativa con las categorías (recodificación a string)
youtube.loc[ (youtube['category_id'] == 1), "category" ] = 'Film & Animation'
youtube.loc[ (youtube['category_id'] == 2), "category" ] = 'Autos & Vehicles'
youtube.loc[ (youtube['category_id'] == 10), "category" ] = 'Music'
youtube.loc[ (youtube['category_id'] == 15), "category" ] = 'Pets & Animals'
youtube.loc[ (youtube['category_id'] == 17), "category" ] = 'Sports'
youtube.loc[ (youtube['category_id'] == 19), "category" ] = 'Short Movies'
youtube.loc[ (youtube['category_id'] == 20), "category" ] = 'Travel & Events'
youtube.loc[ (youtube['category_id'] == 22), "category" ] = 'Gaming'
youtube.loc[ (youtube['category_id'] == 23), "category" ] = 'Videoblogging'
youtube.loc[ (youtube['category_id'] == 24), "category" ] = 'People & Blogs'
youtube.loc[ (youtube['category_id'] == 25), "category" ] = 'Comedy'
youtube.loc[ (youtube['category_id'] == 26), "category" ] = 'Entertainment'
youtube.loc[ (youtube['category_id'] == 27), "category" ] = 'News & Politics'
youtube.loc[ (youtube['category_id'] == 28), "category" ] = 'Howto & Style'
youtube.loc[ (youtube['category_id'] == 29), "category" ] = 'Education'
youtube.loc[ (youtube['category_id'] == 43), "category" ] = 'Science & Technology'

#Creamos una lista con categorías con texto reducido
bar_list = ['Films','Autos','Music','Pets','Sports','Short Movies','Travel','Gaming','Videoblogging','People','Comedy','Entertainment','News & Politics','Howto ','Education','S & T']

#Dibujamos gráfico de barras
plt.barh(bar_list,mytable2)
plt.show()

pd.crosstab(youtube.category_id, youtube.category)
mytable9= mytable2.sort_values()   #Para que se muestren ordenados por tamaño
plt.barh(bar_list,mytable9)  #Habría que ordenar la lista siguiendo el mismo orden

