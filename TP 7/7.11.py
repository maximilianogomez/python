#Ejercicio 11: Dada una lista ordenada de números llamada A y un nuevo número N, desarrollar un programa que agregue el elemento N dentro de la lista A, respetando el ordenamiento existente.
#El programa deberá detectar automáticamente si el ordenamiento es ascendente o descendente antes de realizar la inserción.

#Funcion generar lista:
def genLista():
    #lista vacia
    lista = []
    #condicion para el while que no sea -1
    nro = int(input("Ingrese un numero entero(-1 finalizar): "))
    while nro != -1:
        lista.append(nro)
        nro = int(input("Ingrese un numero entero(-1 finalizar): "))
    return lista

#Funcion ordenamiento ascendente(menor a mayor):
def metodoburbujeo1(lista):
    ordenado = 1
    while ordenado == 1:
        ordenado = 0
        for i in range(len(lista)-1):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                ordenado = 1
    return lista

#Metodo ordenamiento descendiente(mayor a menor):
def metodoburbujeo2(lista):
    ordenado = 1
    while ordenado == 1:
        ordenado = 0
        for i in range(len(lista)-1):
            if lista[i] < lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                ordenado = 1
    return lista
        


#Programa principal:
numeros = genLista()
print("La lista sin el numero agregado: ",numeros)
nro = int(input("Ingrese un numero para agregarlo a la lista: "))
numeros.append(nro)
#ordeno de forma ascendente
inters = metodoburbujeo1(numeros)
print("En ordenamiento ascendente es: ", inters)
inters = metodoburbujeo2(inters)
#ordeno de forma descendiente
print("En ordenamiento descendiente es: ",inters)
