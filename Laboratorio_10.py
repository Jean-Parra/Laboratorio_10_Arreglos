# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:13:14 2020

@author: Jean Parra
"""

import numpy as np        

def norm_arreglo(arreglo):        #declaramos una funcion para la estandarizacion de los datos almacenados
    normalizacion = np.zeros(len(arreglo))      #utilizamos una variable que es igual a una funcion importante de numpy que es "zeros" de la longitud del arreglo
    
    for i in range(0,len(arreglo)):       #aplicamos un ciclo con rango de la longitud del arreglo establecido
        normalizacion[i] = (arreglo[i]-mean_arreglo(arreglo))/std_arreglo(arreglo)      #ponemos una variable de las posiciones que es igual a las posiciones del arreglo menos el promedio,dividido en la desviacion
    return normalizacion     #retornamos la la variable establecida de la operacion 


def std_arreglo(arreglo):       #declaramos una funcion para la desviacion de los datos almacenados
    acum = 0         #utilizamos un acumulador para acumular los resultados de las operaciones
    for i in range(len(arreglo)):       #hacemos un ciclo con rango de la longitud del arreglo establecido
       acum = (arreglo[i]-mean_arreglo(arreglo))**2 + acum      #utilizadndo la operacion de la desviacion se la sumamos a la variable acum
       rta = acum/len(arreglo)    #utilizamos otra variable para el resultado del acumulador dividido en la longitud del arreglo
       desviacion = rta **(1/2)     #le sacamos la raiz cuadrada para terminar la formula de desviacion
    return desviacion      #retornamos a la variable de desviacion

     
def a_power_b(a,b,resultado):      #ponemos una funcion para calcular los resultados de las potencias
    for i in range(b):      #hacemos un ciclo for con rango de el exponente establecido
        resultado = resultado*a       #utilizamos una variable que calcule los resultados
    return resultado        #retornamos a la variable establecida

l = 1        #ponemos una variable igual a 1 que son la cantidad de vueltas
cont = 0       #un contador que cuente la cantidad de resultados pares e impares
pares = 0       #un contador que cuente la cantidad de resultados pares
impares = 0      #un contador que cuente la cantidad de resultados impares


while l < 5:       #un ciclo con una condicion que solo permite seguir si la cantidad de vueltas es mayor igual a 5
    print("recuerde que minimo son 5 vueltas")      #imprimimos un mensaje al usuario recordandole que minimo son 5 vueltas
    l = int(input("ingrese la cantidad de vueltas que quiere: "))      #le pedimos al usuario ingresar la cantidad de vueltas
Arreglo_a = np.zeros(l)     #declaro un agreglo para los numeros bases y lo igualo a la funcion de numpy "zeros" para tener el dato de ubicacion
Arreglo_b = np.zeros(l)     #declaramos un agreglo para los numeros exponentes y lo igualo a la funcion de numpy "zeros" para tener el dato de ubicacion
for i in range(l):      #se realiza un ciclo con rango a la cantidad de vueltas establecidas
    a = int(input("ingrese el numero base: "))     #le pedimos al usuario ingresar el numero base
    Arreglo_a[i]=a     #utilizamos el arreglo con la primera posicion y lo igualamos a la variable a
    b = int(input("ingrese el numero de exponente: "))    #le pedimos al usuario ingresar el numero de exponente
    Arreglo_b[i]=b     #utilizamos el arrelo con la primera posicion y lo igualamos a la variable b
    resultado = 1        #ponemos una variable para los resultados igual a 1
    print("la potencia es: " + str(a_power_b(a,b,resultado)))     #se imprime la funcion que es el resultado de las potencias
    if a_power_b(a, b, resultado) % 2 == 0:      #se utiliza una condicion que consiste en que si la funcion es divisible en 2 y da 0 
        pares = pares + 1        #si la condicion se cumple se le suma 1 al contador pares
    if a_power_b(a, b, resultado) % 2 != 0:     #se utiliza una condicion que consiste en que si la funcion es divisible en 2 y la diferente de 0
        impares = impares + 1        #si la condicion se cumple se le suma 1 al contador de impares
    cont = cont + 1         #independientemente de que sean pares o impares de le suma 1 al contador cont
print("las veces que se ejecutaron fueron: " + str(cont))     #se imprime las cantidad del contador cont
print("los resultados pares fueron: " + str(pares))        #se imprime las cantidades de resultados pares
print("las resultados impares fueron: " + str(impares))       #se imprime la cantidad de resultados impares
print("las posiciones de las bases son: ",(Arreglo_a))    #se imprime las posiciones de las bases
print("las posiciones de los exponentes son: ",(Arreglo_b))      #se imprime las posiciones de los exponentes

def mean_arreglo(arreglos):     #se nombra una nueva funcion para el promedio
    long = len(arreglos)        #ponemos que la variable es igual a la longitud del arreglo establecido
    sumatoria = 0          #utilizamos una variable que es la sumatoria de las posiciones de los arreglos
    for i in range (0,long):       #se aplica un ciclo con rango de la longitud de los arreglos
        sumatoria = sumatoria + arreglos[i]     #utilizamos las posiciones de los arreglos y se los sumamos a la variable sumatoria
    return sumatoria/long       #retornamos a la sumatoria dividida en la longitud de los arreglos

print("promedio arreglo a: ", mean_arreglo(Arreglo_a))       #imprimimos el promedio del arreglo de las bases con la funcion de promedio establecida
print("promedio arreglo b: ", mean_arreglo(Arreglo_b))        #imprimimos el promedio del arreglo de los exponentes con la funcion de promedio establecida

Aa = float(mean_arreglo(Arreglo_a))      #declaramos una variable que es igual al promedio del arreglo de las bases
Bb = int(mean_arreglo(Arreglo_b))       #declaramos una variable que es igual al promedio del arreglo de los exponentes

print("potencia de b promedio de a promedio", a_power_b(Aa,Bb,1))     #imprimimos la potencia de los exponentes promedio de las bases promedio con la funcion de calcular las potencias

std_arreglo(Arreglo_a)     #declaramos la funcion de desviacion con el arreglo de las bases
print("la desviacion estandar del primer arreglo es: ",std_arreglo(Arreglo_a))     #imprimimos la desviacion estantar del arreglo de las bases
std_arreglo(Arreglo_b)     #declaramos la funcion de desviacion con el arreglo de los exponentes
print("la desviacion estandar del segundo arreglo es: ",std_arreglo(Arreglo_b))     #imprimimos la desviacion estantarde del arreglo de los exponentes

norm_arreglo(Arreglo_a)       #declaramos la funcion de normalidad del arreglo de las bases 
print("la normalizacion a: ",norm_arreglo(Arreglo_a))      #imprimimos la normalizacion del arreglo de las bases
norm_arreglo(Arreglo_b)       #declaramos la funcion de normalizacion del arreglo de los exponentes
print("la normalizacion b: ",norm_arreglo(Arreglo_b))     #imprimimos la normalizacion del arreglo de los exponentes


print("el nuevo promedio a es: ",int(mean_arreglo(norm_arreglo(Arreglo_a))))       #imprimimos el nuevo promedio con la funcion del promedio en la normalizacion de arrelo de las bases
print("el nuevo promedio b es: ",int(mean_arreglo(norm_arreglo(Arreglo_b))))       #imprimimos el nuevo promedio con la funcion del promedio en la normalizacion del arreglo de los exponentes
print("la nueva desviacion es: ",int(std_arreglo(norm_arreglo(Arreglo_a))))        #imprimimos la nueva desviacion con la funcion de desviacion en la normalizacion del arreglo de las bases
print("la nueva desviacion es: ",int(std_arreglo(norm_arreglo(Arreglo_b))))        #imprimimos la nueva desviacion con la funcion de desviavion en la normalizacion del arreglo de los exponentes
