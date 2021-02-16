#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:01:48 2020

@author: carlosdonosocabero

LOOPS
"""
#reset -f 

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

""""
FOR loops

""""

for i in range(0,11,1):  #Implícito el rango
    print("i:",i)
    
for i in [1,2,3,4]:  #Explícito el rango
    print("i:",i)

for i in ['red', 'blue', 'yellow']:
    print('Y el color es:',i)

for i in ['red', 'blue', 'yellow']:
    print(i)

for i in range(0,11,1):
    print("i:",i)
    
    print('Hello world')
    
    x = wbr['cnt']
    plt.hist(x, bins=10)
    plt.show()

for i in range(10,101,1):
    
    x = wbr['cnt']
    plt.hist(x, bins=i)
    plt.show()
    print(i)

for i in range(20,2,-1):
    
    x = wbr['cnt']
    plt.hist(x, bins=i)
    plt.show()
    print(i)

#Dibujar    
ax = plt.subplots(figsize=(9, 9)) #Define plot size
ax = plt.gca() #Create emty plot
# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

c1=plt.Circle((5, 5), 1, alpha=1, color='r') #Define  circle (coordenadas x e y, radio, transparencia y color)
ax.add_artist(c1)  #Draw circle

#Con bucle for para poner todos los círculos en la diagonal principal
ax = plt.subplots(figsize=(9, 9)) #Define plot size
ax = plt.gca() #Create emty plot
# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

for i in range(0,11,1):
    c1=plt.Circle((i, i), 0.5, alpha=1, color='r')
    ax.add_artist(c1)

#Con "animación"
ax = plt.subplots(figsize=(9, 9)) #Define plot size
ax = plt.gca() #Create emty plot
# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

for i in range(0,11,1):
    c0=plt.Circle((i-1, i-1), 0.4, alpha=1, color='w')
    c1=plt.Circle((i, i), 0.5, alpha=1, color='r')
    ax.add_artist(c0)
    ax.add_artist(c1)

ax = plt.subplots(figsize=(9, 9)) #Define plot size
ax = plt.gca() #Create emty plot
# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

#Doble dibujo sobre las dos diagonales
ax = plt.subplots(figsize=(9, 9)) #Define plot size
ax = plt.gca() #Create emty plot
# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

for i in range(0,11,1):
    c1=plt.Circle((i, i), 0.5, alpha=1, color='r')
    c2=plt.Circle((i, 10-i), 0.5, alpha=1, color='b')
    ax.add_artist(c1)
    ax.add_artist(c2)
    
#Crecimiento de los círculos
ax = plt.subplots(figsize=(9, 9)) #Define plot size
ax = plt.gca() #Create emty plot
# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

for i in range(0,11,1):
    c1=plt.Circle((i, i), i/10, alpha=1, color='r')
    ax.add_artist(c1)

#Cambiar los colores también, así como el grado de transparencia (que varía entre 0-1)
colors=['b','g','r','c','m','y','orange','maroon','darkgreen','aquamarine','k']

ax = plt.subplots(figsize=(9, 9)) #Define plot size
ax = plt.gca() #Create emty plot
# change default range so that new circles will work
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

for i in range(0,11,1):
    c1=plt.Circle((i, i), i/10, alpha=i/10, color=colors[i])
    ax.add_artist(c1)
    

"""
WHILE loops 

Cuando queremos repetir un proceso 'mientras' se cumpla una condición concreta)
"""   
    
count=1  #Initialize counter
while(count<4):  #Control condition
    print(count,'Calidad')  #Action
    count= count+1  #Counter increase
print('Mi contador vale:', count)


""""
IF loops

Ejecución condicional

""""

##Control Flow###

#Examples

result_covid = ["negativo"]

if result_covid == 'negativo':
    print ("Puede usted salir de casa")
else:
    print("Debe quedarse en casa")
    

test_covid = 0

if test_covid == 0:
    print ("Puede usted salir de casa")
else:
    print("Debe quedarse en casa")
    

# for + if
  
for i in range (0,11,1):
    print ("My grade is: " , i)
    
    if i >= 5:
        print ("Aprobado!")
    else:
        print("Suspenso...")
        

for i in range (0,11,1):
    if i < 5:
        grade = "Fail"
    else:
        grade = "Pass"
    print ("My grade is ", i , ":", grade)
      

for i in range (0,11,1):
    
    if i < 5:
        grade = "Fail"
    elif  4 < i < 7:
        grade = "Pass"
    elif 6 < i < 9:
        grade = "Notable"
    elif 8 < i < 11:
        grade = "Excellent"
        
    print ("My grade is ", i , ":", grade)

    