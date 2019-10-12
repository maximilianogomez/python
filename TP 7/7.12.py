#Ejercicio 12: Leer una lista de números V. Luego se solicita:

#• Calcular el producto de los elementos de subíndice par y dividirlo por la suma de los elementos de subíndice impar, sólo si esta suma es distinta de cero.

#Imprimir la lista leída y el resultado calculado, o un mensaje de error en caso de no poder realizar la operación. 
 
#• Generar e imprimir otra lista tal que su primer elemento contenga la suma del primero más el último elemento de la lista V; el segundo elemento contenga la suma del segundo más el penúltimo de V, etc.

#La nueva lista contendrá la mitad de los elementos de la lista original. 
 
#• Imprimir un listado de aquellos elementos de V que cumplan con la condición de tener iguales sus dos elementos laterales (el anterior y el siguiente).

#Si ninguno cumple esta condición, se imprimirá una leyenda aclaratoria.

#Considerar que los extremos de la lista se encuentran unidos, de modo que el último elemento se encuentra antes que el primero, y que el primer elemento se encuentra después del último.


#Funcion generarlista:
def genLista():
    #creo una lista vacia
    V = []
    nro = int(input("Ingrese un numero (-1 para finalizar): "))
    while nro != -1:
        #genero numeros mientras sean distintos a -1
        V.append(nro)
        nro = int(input("Ingrese un numero (-1 para finalizar): "))
    return V

#Funcion 1:
def sumaC(lista):
    #suma de los impares
    suma = 0
    #producto de los enteros
    prod = 1
    for i in range(len(lista)):
        if i % 2 == 0:
            prod *= lista[i]
        else:
            suma += lista[i]
    if suma != 0:
        r = prod / suma
        return r
    else:
        print("La suma de los numeros de subindice impar es 0")
    
        
#Funcion 2:
def sumaRara(lista):
    #genero una lista
    rara = []
    i = 0
    k = len(lista) - 1
    while i <= (len(lista)//2) and k >= (len(lista)//2):
        suma = lista[i] + lista[k]
        rara.append(suma)
        suma = 0
        i += 1
        k -= 1
    return rara

#Funcion 3:
def elemLaterales(lista):
    #genero una lista nueva
    nova = []
    #busqueda secuencial comparando elementos
    for i in range(0, len(lista)):
        if i==0: #es el primer elemento de la lista
            if lista[i] == lista[len(lista)-1] and lista[i] == lista[i+1]:
                nova.append(lista[i])
                
        elif i == len(lista)-1 : #Es el ultimo elemento de la lista
            if lista[i] == lista[i-1] and lista[i] == lista[0] :
                nova.append(lista[i])
        else: #es un valor cualquiera
            if lista[i-1] == lista[i] and lista[i]==lista[i+1]:
                nova.append(lista[i])
    return nova
                
        
#Programa principal:
numeros = genLista()
print(numeros)
r1 = sumaC(numeros)
print(r1)
r2 = sumaRara(numeros)
print("La suma del primer elemento con el ultimo, el segundo con el anteultimo y etc es: ",r2)
r3 = elemLaterales(numeros)
print("La lista con los elementos laterales es: ", r3)
    
 

