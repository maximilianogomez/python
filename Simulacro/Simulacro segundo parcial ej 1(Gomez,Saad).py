'''Desarrollar un programa que genere números enteros al azar entre 1 y
100 hasta que se genere el cero. Informar cuántos elementos se
crearon y Mostrar la lista por pantalla (1,5 pto)
Luego informar:
a) El promedio y los elementos mayores al promedio informando en que
lugar se ubicaron en la lista. (1,5 pto)
b) Desarrollar una función para eliminar de la lista todos los valores impares y retorne
la cantidad de elementos que eliminó de la lista. Mostrar la lista antes y despues de
eliminar los elementis (2 ptos) '''

import random

#funcion generar lista:
def genLista():
    lista = []
    cont = 0
    nro = random.randint(0,100)
    if nro == 0:
        cont += 1
    else:
        while nro != 0:
            lista.append(nro)
            cont += 1
            nro = random.randint(0,100)
    return lista, cont
    
#Funcion promedio:
def prom(lista, cont):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    promedio = (suma) / cont
    return promedio

#funcion mayor al promedio:
def analisisProm(lista,promedio):
    mayoralProm = []
    for i in range(len(lista)):
        if lista[i] > promedio:
            mayoralProm.append(i)
    return mayoralProm

#funcion eliminar valores:
def eliminarImpares(lista):
    cont = 0
    i = len(lista) - 1
    while i > 0:
        if i % 2 != 0:
            lista.pop(i)
            cont += 1
        i -= 1
            
    return lista, cont

#Programa Principal:
numeros, cantidad = genLista()
promedio = prom(numeros , cantidad)
mayorProm = analisisProm(numeros, promedio)
print("El promedio general de la lista es: ", promedio)
print("La lista con los indices de los numeros mayores al promedio es: ", mayorProm)
print("La lista es : ", numeros, " y la cantidad de elemntos es: ", cantidad)
listafinal, eliminados = eliminarImpares(numeros)
print("La lista Final con los elementos impares eliminados es: ", listafinal)
print("La cantidad de elementos eliminados fueron: ", eliminados)
    





            
            
            

            