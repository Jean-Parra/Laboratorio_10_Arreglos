# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:13:14 2020

@author: Jean Parra
"""

def a_power_b(a,b,resultado):         #declaramos una funcion 
    for i in range(b):         #utilizamos el mismo ciclo que repeticion 
        resultado = resultado*a        #la variable que calcula las multiplicaciones hasta el rango de la exponente
    return resultado         #se retorna todas las multiplicaciones realizadas

a = 1         #declaranos la variable base igual a 1 para que entre al proximo ciclo
while a!= 0:         #realizamos un ciclo while para que se repita n veces hasta que el usuario ponga 0 en la base
    a = int(input("ingrese el numero base: "))      #le pidimos al usuario ingresar un numero de base
    b = int(input("ingrese el numero de exponente: "))       #le pidimos al usuario ingresar un numero de exponente
    resultado = 1         #declaramos la variable de multiplicacion igual a uno para que se realize correctamente
    print("la potencia es: " + str(a_power_b(a,b,resultado)))       #imprimimos la funcion establecida que es el resultado de todas las vueltas
