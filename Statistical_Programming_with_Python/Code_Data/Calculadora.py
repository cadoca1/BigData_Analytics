#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 20:37:27 2021

@author: carlosdonosocabero
"""

print('**** Mi Calculadora ****')
print('Operaciones aritméticas básicas')
print('1-Suma')
print('2-Resta')
print('3-Multiplicación')
print('4-División')
print('5-Potencia')
print('6-Salir de Mi Calculadora')

x = int(input('Elige una operación: '))

if (x==1):
    a = float(input('Introduce el primer número de la suma: '))
    b = float(input('Introduce el segundo número de la suma: '))
    resultado = a + b
    print('El resultado es:', resultado)
    x = int(input('Elige una operación: '))
elif (x==2):
    a = float(input('Introduce el primer número de la resta: '))
    b = float(input('Introduce el segundo número de la resta: '))
    resultado = a - b
    print('El resultado es:', resultado)
    x = int(input('Elige una operación: '))
elif (x==3):
    a = float(input('Introduce el primer número de la multiplicación: '))
    b = float(input('Introduce el segundo número de la multiplicación: '))
    resultado = a * b
    print('El resultado es:', resultado)
    x = int(input('Elige una operación: '))
elif (x==4):
    a = float(input('Introduce el dividendo de la división: '))
    b = float(input('Introduce el divisor de la división: ')) 
    resultado = a / b
    print('El resultado es:', resultado)
    x = int(input('Elige una operación: '))
elif (x==5):
    a = float(input('Introduce la base de la potencia: '))
    b = float(input('Introduce el exponente de la potencia: '))
    resultado = a ** b
    print('El resultado es:', resultado)
    x = int(input('Elige una operación: '))
elif (x==6):
    print('Gracias por usar Mi Calculadora')
elif (x>6):
    print('Syntax Error')
    x = int(input('Elige una operación: '))

#%%

