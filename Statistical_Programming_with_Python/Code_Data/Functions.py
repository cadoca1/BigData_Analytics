#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:13:24 2020

@author: carlosdonosocabero
"""

##### FUNCTIONS IN PYTHON ######

#Define la función 'sumar':

def plus (a, b):
    a + b
    print ("El resultado de mi suma es:")
    return a + b       
        
print (plus(2,3))

#%%

#Define la función  'división':

def dividir (a,b):  #Podemos comentar al principio:
        """Podemos escribir comentarios a mitad para explicar"""
        a / b
        print ("El resultado de mi división es:")
        return a / b

print (dividir(12,3))
