#Ejercicio 10: Cargar dos listas de números A y B. Se solicita construir e imprimir tres nuevas listas que contengan:
#• La concatenación de los valores pares de A con los impares de B.*
#• La concatenación de los valores pares de A con el reverso de los valores pares de B. ("valores pares" o "valores impares" se refiere a los elementos propiamente dichos y no a sus posiciones).
#• La intercalación de los elementos de A y B.

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

#Funcion lista 1:
def concatenacion1(lista1,lista2):
    #creo la lista concatenacion1
    conc1 = []
    for i in range(len(lista1)):
        #si el valor es par lo agrego
        if lista1[i] % 2 == 0:
            conc1.append(lista1[i])
    for j in range(len(lista2)):
        #si el valor es impar lo agrego
        if lista2[j] % 2 != 0:
            conc1.append(lista2[j])
    return conc1
#Funcion lista2:
def concatenacion2(lista1,lista2):
    #creo una lista concatenacion2
    conc2 = []
    numinverso = 0
    for i in range(len(lista1)):
        #si el valor es par lo agrego
        if lista1[i] % 2 == 0:
            conc2.append(lista1[i])
    for j in range(len(lista2)):
        #analizo los valores pares de B
        if lista2[j] % 2 == 0:
            #guardo el valor de la lista para no perder el valor
            aux = lista2[j]
            #revierto el valor par de B
            while lista2[j] != 0:
                dig = lista2[j] % 10
                lista2[j] //= 10
                numinverso = (numinverso * 10) + dig
            #llamo a la funcion auxiliar para devolverle el valor original a lista2[j]
            lista2[j] = aux
            #agrego el inverso
            if numinverso == lista2[j]:
                #si el numero solo tiene un digito lo multiplico por 10 (ej: 02 , invertido quedaría 20)
               numinverso *= 10
               conc2.append(numinverso)
            else:
                conc2.append(numinverso)
            numinverso = 0
    return conc2

#Funcion lista3(concatenación de los elementos intercalados):
def intercalar(lista1,lista2):
    #creo una lista vacia
    inter = []
    i = 0
    j = 0
    while i < len(lista1) and j < len(lista2):
        #recorre la lista desde 0 hasta sus ultimos elementos y los agrega a la lista creada intercalar
        inter.append(lista1[i])
        inter.append(lista2[j])
        i += 1
        j += 1
    return inter
           
    
#Programa Principal:
print("Ingrese los valores para crear la lista A")
A = genLista()
print("Ingrese los valores para crear la lista B")
B = genLista()
print("lista A: ", A)
print("lista B: ", B)
r1 = concatenacion1(A,B)
print("La concatenacion de los pares de A y los impares de B: ",r1)
r2 = concatenacion2(A,B)
print("La concatenación de los valores pares de A con el reverso de los valores pares de B: ", r2)
r3 = intercalar(A,B)
print("La intercalación de los elementos de A y B: ", r3)


        
        

    