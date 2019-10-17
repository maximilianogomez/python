#Ejercicio 13: Realizar un programa que permita ingresar números en una lista, finalizando la lectura con -1.
#Informar si la secuencia de elementos ingresada es ascendente, descendente, todos sus valores son iguales o se encuentra desordenada.

#funcion generar lista
def genLista():
    #creo una lista vacia
    lista = []
    nro = int(input("Ingrese un numero (-1 para terminar): "))
    #analizo el nro para ver si se cargo algo
    if nro == -1:
        print("todavia no cargo ningún número a la lista")
    else:
        while nro != -1:
            #proceso el numero y si es != -1 lo agrego a la lista
            lista.append(nro)
            nro = int(input("Ingrese un numero (-1 para terminar): "))
        return lista

#busqueda secuencial descendente:
def bssecDesc(lista):
    #comparo numero a numero
    for i in range(len(lista) - 1):
        for k in range(i + 1, len(lista)):
            #si el primero es mayor que el segundo es verdadero
            if lista[i] > lista[k]:
                z = True
            else:
                #si no lo es, quiero que devuelva un falso y termine el ciclo
                z = False
                return z
    return z
#busqueda secuencial valores iguales:
def bssecIgual(lista):
    #comparo numero a numero
    for i in range(len(lista) - 1):
        for k in range(i + 1, len(lista)):
            #si el primero es igual que el segundo es verdadero
            if lista[i] == lista[k]:
                z = True
            else:
                #si no lo es, quiero que devuelva un falso y termine el ciclo
                z = False
                return z
    return z


#busqueda secuencial ascendente:
def bssecAsc(lista):
    #comparo numero a numero
    for i in range(len(lista) - 1):
        for k in range(i + 1, len(lista)):
            #si el primero es menor que el segundo es verdadero
            if lista[i] < lista[k]:
                z = True
            else:
                #si no lo es, quiero que devuelva un falso y termine el ciclo
                z = False
                return z
    return z

#Programa Principal:
#genero una lista
numeros = genLista()
#analizo si esa lista es descendente
if bssecDesc(numeros) == True:
    print("La lista es descendente")
#analizo si es ascendente
elif bssecAsc(numeros) == True:
    print("La lista es ascendente")
#analizo si todos sus valores son iguales
elif bssecIgual(numeros) == True:
    print("Todos sus valores son iguales")
else:
    #si no es ninguna esta desordenada
    print("La lista está desordenada")

        