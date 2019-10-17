#Ejercicio 15: Leer dos listas de números M y N, ambas ordenadas de menor a mayor.
#Generar e imprimir una tercera lista que resulte de intercalar los elementos de M y N. La nueva lista también debe quedar ordenada, sin utilizar ningún método de ordenamiento.

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
    
#funcion ordenamiento:
def secuencial(lista):
    for i in range(len(lista)-1):
        for k in range(i + 1, len(lista)):
            if lista[i] > lista[k]:
                aux = lista[i]
                lista[i] = lista[k]
                lista[k] = aux
    return lista

#funcion intercalar:
def intercalar(lista1, lista2):
    r = []
    i = 0
    k = 0
    while i < len(lista1) and k < len(lista2):
        r.append(lista1[i])
        r.append(lista2[k])
        i += 1
        k += 1
    return r

#Programa principal:
print("Se creara la lista M")
M = genLista()
print("Se creara la lista N")
N = genLista()
Mord = secuencial(M)
Nord = secuencial(N)
print("La lista M: ", Mord)
print("La lista N: ", Nord)
rta = intercalar(Mord,Nord)
print("La lista intercalada es: ", rta)