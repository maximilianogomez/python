#Ejercicio 9: Dado una lista de N números (por ejemplo 5), devolver una lista de N-1 valores booleanos,
#tal que cada valor de este último arreglo corresponde al resultado de la comparación de los pares de valores consecutivos del primer arreglo.
#El valor booleano es True si el primer elemento del par es menor o igual que el siguiente, y False si no lo es

#Funcion generar lista:
def genLista():
    #creamos lista vacia
    lista = []
    #pedimos numero
    n = int(input("Ingrese cuantos numeros tendra su lista: "))
    for i in range(n):
        #procesar dato
        nro = int(input("Ingrese un numero: "))
        lista.append(nro)
    return lista

#Funcion comparacion valores:
def compValores(lista):
    #creo la nueva lista
    bool = []
    for i in range(len(lista) - 1):
        #comparo los valores siguientes
        if lista[i] <= lista[i + 1]:
            bool.append(True)
        else:
            bool.append(False)
    return bool
#Programa Principal:
numeros = genLista()
print(numeros)
listaBool = compValores(numeros)
print(listaBool)


        
    