# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:13:14 2020

@author: Jean Parra
"""

def a_power_b(a,b,resultado):       #se declara la funcion
    for i in range(b):           #un ciclo que se repita las cantidades que se multiplica
        resultado = resultado*a       #una variable que calcula dicha multiplicacion
    return resultado         #retorna el total, que es la potencia

a = int(input("ingrese el numero base: "))         #se le pide al usuario ingresar un numero de base
b = int(input("ingrese el numero de exponente: "))       #se le pide al usuario ingresar un numero de exponente
resultado = 1           #tenemos la variable igual a uno para que multiplique adecuadamente

print("la potencia es: " + str (a_power_b(a,b,resultado)))      #imprimirnos la funcion que es el resultado de la potencia




