#Ejercicio 8: Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir el valor mínimo y el lugar que ocupa.
#Tener en cuenta que el mínimo puede estar repetido, en cuyo caso deberán mostrarse todas las posiciones que ocupe.
#La carga de datos termina cuando se obtenga un 0 como número al azar, el que no deberá cargarse en la lista.

import random
#Funcion generar lista:
def genLista():
    #creo una lista vacia
    lista = []
    i = 0
    lista.append(random.randint(0,100))
    #le doy valores hasta el 0:
    while i < len(lista) and lista[i] != 0:
        lista.append(random.randint(0,100))
        i += 1
    lista.pop(len(lista)-1)
    return lista

#Funcion hallar minimo:
def minimo(lista):
    #Establezco el minimo como el primer valor
    min = lista[0]
    for i in range(len(lista)):
        #Si encentro un valor mas bajo, actualizo el minimo
        if lista[i] < min:
            min = lista[i]
    return min
#Funcion lista con los minimos:
def listaMin(lista,min):
    #creo una lista vacia donde pondre las posiciones
    pos = []
    i = 0
    while i < len(lista):
        #busco en la lista los minimos y si los encuentra los agrego a mi lista.
        if lista[i] == min:
            pos.append(i)
        i += 1
    return pos

#Programa Principal:
numeros = genLista()
print(numeros)
#Hallo los mínimos y sus posiciones:
min = minimo(numeros)
#generó la lista con las posiciones en la que se encuentra el mínimo:
listaPos = listaMin(numeros, min)
print("El valor mínimo", min," de la lista se encuentra en las posiciones: ", listaPos)
 
    
            
        


    