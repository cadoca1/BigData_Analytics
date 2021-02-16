t# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Our first dataset
Update 2020_10_03 Kick off PEP
"""

#%reset -f

3
3+2
a=3
b=2
c=a+b
c
print(c)

a
b
print(a)
print(b)

a='Hello'
b='World'
c=' '

print(a)
print(b)

d=a+c+b
print(d)    #También se puede escribir al lado de una instrucción
print(a,b)

#Vamos a saludar al mundo

del(a,b,c,d)
a


#%reset -f

#Load basic libraries
import os  #sistema operativo
import pandas as pd  #le llama así a pandas, que sirve para gestionar matrices de datos desde Python
import numpy as np  #operaciones numéricas
import matplotlib.pyplot as plt  #gráficas

#Create a dataframe for the class
#Lists are defined in Python with [], separated by commas

name=['Yaling', 'Sofía', 'Maria', 'Pablo', 'Inés'] #Las listas son colección de valores, separados con comas
print(name)
name[1]
name[0]  #Siempre se empieza a contar desde 0, no desde 1
name(2)  #No funciona porque no está entre corchetes
name[0]+name[1]

name=['Yaling', 'Sofía', 'Maria', 'Pablo', 'Inés']
age=[28,23,25,23,25]
gender=['Female','Female','Female','Male','Female']


print(name, age, gender)

class2020= pd.DataFrame({'name': name, 'age': age, 'gender': gender})

#Clean up
del(age, gender, name)

class2020.age  #Para acceder a los datos de dentro, aquí la segunda columna

class2020.shape  #Filas por columnas
dimensiones= class2020.shape
dimensiones[0]  #Para sacar de dentro de una variable usar []
del(dimensiones)

class2020.head()  #Los primeros valores
class2020.head(3)

class2020.tail()  #Los últimos valores
class2020.tail(1)  

#QC OK  Quiere decir que después de analizar shape, head y tail ya he hecho un control de calidad



edad = class2020.age
edad
del(edad)


#Get working directory
os.getcwd()

#Change working directory 
os.chdir('/Users/carlosdonosocabero/Desktop/MDA/PEP/CodeyData')
os.getcwd()

#Guardar
class2020.to_excel('class2020.xlsx')
class2020.to_csv('class2020.csv')

#Para importar un Excel
df= pd.read_excel('class2020.xlsx')  
