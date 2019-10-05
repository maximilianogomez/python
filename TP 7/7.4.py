#Ejercicio 4: Invertir aquellos valores ubicados en posiciones impares de una lista.

#Funcion invertir:
def esImpar(n):
    for i in range(len(n)):
        #pedimos las i impares
        if i % 2 != 0:
            #invertimos a la -1 los valores impares
            n[i] = n[i] ** (-1)
    return n

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
        
#Programa principal:
numeros = genLista()
print(numeros)
numeros = esImpar(numeros)
print(numeros)