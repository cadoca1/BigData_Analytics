#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:49:15 2021

@author: carlosdonosocabero
"""
#%reset -f

def Menu():
    """Función que muestra el Menú"""
    print ("""************
Mi Calculadora
************
Menú:
1) Suma
2) Resta
3) Multiplicación
4) División
5) Potencia
6) Salir """)

def Calculadora():
    """Realiza aquí tus operaciones aritméticas"""
    Menu()
    opc = int(input("Selecciona opción\n"))
    while (opc >0 and opc <6):
        if (opc==1):
            x = float(input("Introduce el primer número de la suma:\n"))
            y = float(input("Introduzca el segundo número de la suma:\n"))
            print ("El resultado es:", x+y)
            opc = int(input("Selecciona opción\n"))
        elif(opc==2):
            x = float(input("Introduce el primer número de la resta:\n"))
            y = float(input("Introduce el segundo número de la resta:\n"))
            print ("El resultado es:",x-y)
            opc = int(input("Selecciona opción\n"))
        elif(opc==3):
            x = float(input("Introduce el primer número de la multiplicación:\n"))
            y = float(input("Introduce el segundo número de la multiplicación:\n"))
            print ("El resultado es:",x*y)
            opc = int(input("Selecciona opción\n"))
        elif(opc==4):
            x = float(input("Introduce el dividendo de la división:\n"))
            y = float(input("Introduce el divisor de la división:\n"))
            try:
              print ("El resultado es:", x/y)
              opc = int(input("Selecciona opción\n"))
            except ZeroDivisionError:
              print ("No se permite la división entre 0")
              opc = int(input("Selecciona opción\n"))
        elif(opc==5):
            x = float(input("Introduce la base de la potencia:\n"))
            y = float(input("Introduce el exponente de la potencia:\n"))
            print ("El resultado es:",x**y)
            opc = int(input("Selecciona opción\n"))

Calculadora()
