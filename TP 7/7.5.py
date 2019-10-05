#Ejercicio 5: Escribir una función para devolver la posición que ocupa un valor pasado como parámetro, utilizando búsqueda secuencial en una lista desordenada.
#La función debe devolver -1 si el elemento no se encuentra en la lista.

#Funcion generarlista:
def genLista():
    #creamos lista vacia
    lista = []
    #pedimos numero
    nro = int(input("Ingrese un numero (-1 para finalizar): "))
    while nro != -1:
        #procesar dato
        lista.append(nro)
        nro = int(input("Ingrese un numero(-1 para finalizar): "))
    return lista
#Funcion busqueda secuencial:
def busSecuencial(lista,nro):
    i = 0
    #busco en la lista y si el orden no encuentra el numero aumenta el contador
    while i < len(lista) and lista[i] != nro:
        i += 1
    
    #si el contador es igual a la longitud de lista no se encontró
    if i == len(lista):
        encontrado = -1
    else:
        #caso contrario, se encontro el lugar y se devuelve el lugar en la lista
        encontrado = i
    return encontrado

#Programa principal:
numeros = genLista()
print(numeros)
n = int(input("Ingrese el numero a buscar en la lista: "))

if busSecuencial(numeros,n) == -1:
    print("El numero no se encontró en la lista ", busSecuencial(numeros,n))
else:
    print("La posicion en la que está el numero es: ", busSecuencial(numeros,n))

