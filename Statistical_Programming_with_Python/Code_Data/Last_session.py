#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:07:46 2021

@author: carlosdonosocabero

Data containers y objetos
"""
import os

os.getcwd()
os.chdir("/Users/carlosdonosocabero/Desktop/MDA/PEP/CodeyData")


#Variables
print("Hola")
a = input("¿Me podrías decir tu nombre?")
print("Encantado de conocerte", a)
b = int(input("¿Cuántos años tienes?"))  #Por defecto te lo da en string, hay que transformarlo a int
print("¡Casi 25!")

#Lists
age = [23,25,24]
age[0] = 25
age  #Son modificables y accesibles

nom = ["Carlos", "Marcos", "Ulpiano"]

#Tuples: listas que no se pueden modificar
edades_fijas = (28,23,33)  #Se define con paréntesis
edades_fijas[1]  #Se llama con brackets
edades_fijas[1] = 33  #No se pueden modificar

#Pandas DataFrames (estructura de matriz de datos, como Excel)
import pandas as pd
clase2020 = pd.DataFrame({'age':age, 'nombre': nom})  #Incluye un diccionario, otro tipo

clase2020.age  #Extraigo el atributo 'age' de mi objeto clase2020
edad = clase2020.age

print(edad)  #Aplicamos una función externa 'print'
sum(clase2020.age)
sum(edad)  #Lo mismo
len(edad)  #Dice la longitud de una lista
mean(clase2020.age)  #Esta función no está definida en Python

#Pues la creamos ad hoc:
def media (a):
    print('The average is ...')
    return sum(a)/len(a)

media(clase2020.age)  #La nueva función externa definida ataca al atributo del objeto

#Pero también hay métodos, que no son funciones externas

edad.sum()  #La edad se suma a sí misma, es un objeto que contiene información y que además tiene definido internamente un método de suma
edad.len()  #No está definido
edad.count()

#Los métodos acaban en paréntesis por RG, los atributos no

edad.media()  #No puede

#Pues definamos una nueva clase de objetos que sean listas numéricas con media ya precalculada
class lista_pro:
    datos = [20,21,23,34,21]
    
    def media(self):
        print('The average is ...')
        return sum(self.datos)/len(self.datos)

edad1 = lista_pro()  #Es un objeto con datos dentro y que tiene la capacidad de calcularse a sí mismo la media (lleva un método incluido)
edad1.datos  #Atributo
edad1.media()  #Método

print(edad1.datos)
print(edad1.media())      

class lista_pro2:  #La creamos sin datos, para rellenarlos después
    datos = []
    
    def media(self):
        print('The average is ...')
        return sum(self.datos)/len(self.datos)

edad2 = lista_pro2()
edad2.datos = [2,3,4]

edad3 = lista_pro2()
edad3.datos = [5,6,7]  #Dos objetos iguales con datos distintos

edad2.media()
edad3.media()

clase2020.age.describe()  #Python está más bien orientado a métodos (más que a funciones externas)
clase2020.age.sum()

### ORDEN

#Creo una clase en abstracto con datos (vacíos aún) y con métodos
class data_container:
    edad = []
    nombres = []
    
    def media_e(self):
        print('The average is ...')
        return sum(self.edad)/len(self.edad)
    
    def alf(self):
        print('Los nombres:')
        print(sorted(self.nombres))
        
#Creo objeto a partir de la clase     
my_data = data_container()  

#Relleno con datos el objeto
my_data.edad = [1,2]
my_data.nombres  = ['Yo', 'Io']

my_data.alf()  #Método
my_data.nombres  #Atributo
