# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:13:14 2020

@author: Jean Parra
"""

def a_power_b(a,b,resultado):       #declaramos la funcion 
    for i in range(b):         #utilizamos el ciclo para que se repita en un rango del numero de exponente
        resultado = resultado*a         #utilizamos una variable que tenga las multiplicaciones
    return resultado         #retornamos todos los resultados

a = 1        #declaramos que el numero base es igual a uno para que entre al ciclo siguiente
cont = 0      #utilizamos un contador que cuente los resultados pares e impares
pares = 0      #utilizamos otro contador que cuente los resultados pares
impares = 0      #utilizamos otro contador que cuente los resultados impares

while a!= 0:      #utilizamos un cliclo que se repita hasta que el usuario ponga en la base 0
    a = int(input("ingrese el numero base: "))      #le pedimos al usuario poner un numero base
    b = int(input("ingrese el numero de exponente: "))       #le pedimos al usuario poner un numero de exponente
    resultado = 1      #declramos que la variable que multiplicacion es igual a uno para realizar el ciclo
    print("la potencia es: " + str(a_power_b(a,b,resultado)))      #imprimimos la funcion que es el resultado de todas las potencias
    if a_power_b(a, b, resultado) % 2 == 0:       #utilizamos una condicion que consiste, en que si la funcion dividida en 2 es igual a 0 
        pares = pares + 1      #si la condicion se cumple de le suma 1 a la variable pares
    if a_power_b(a, b, resultado) % 2 != 0:     #utilizamos otra condicion que consiste, en que si la funcion dividida en 2 es diferente de 0
        impares = impares + 1      #si esta condicion se cumple le sumamos 1 a la variable impares
    cont = cont + 1       #independiente de que sea par o impar en la variable cont se le suma 1
print("las veces que se ejecutaron fueron: " + str(cont))      #imprimimos la cantidad de la variable cont
print("los resultados pares fueron: " + str(pares))       #imprimimos la cantidad de la variable pares
print("las resultados impares fueron: " + str(impares))        #imprimimos la cantidad de la variable impares
