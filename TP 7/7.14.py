#Ejercicio 14: Eliminar de una lista de números enteros los valores que se encuentren en una segunda lista.
#Imprimir la lista original, la lista de valores a eliminar y la lista resultante.

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
    
#funcion lista resultante
def listaFinal(lista1,lista2):
    #creo la lista resultante con los valores de la original
    k = 0
    while k < len(lista2):
    #si ambos valores son iguales en la lista quiero que se eliminé el valor de la lista creada
        for x in range(len(lista1)):
            if lista1[x] == lista2[k]:
                #borro el valor una vez que lo encuentro y lo añado al final para que no haya errores de rango
                lista1.pop(x)
                lista1.append(lista2[k])
        k += 1
    for i in range(len(lista2)):
        #borro los ultimos valores que agregué
        lista1.pop()
    return lista1



#Programa principal:
#creo la lista original
print("A continuación creará la lista original")
original = genLista()
#creo la lista con los valores a suprimir
print("A continuación creará la lista con los valores a suprimir de la original")
suprimir = genLista()
#imprimo la lista original ya que si no, se perderán sus valores
print("La lista original :" , original)
#llamo a la funcion para mi lista resultante
resultante = listaFinal(original,suprimir)
print("La lista con valores a suprimir : ", suprimir)
print("La lista resultante: ", resultante)


            
    