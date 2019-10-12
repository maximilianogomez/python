import random
#Ejercicio 8: Rellenar una lista con números enteros entre 0 y 100
#obtenidos al azar e imprimir el valor mínimo y el lugar
#que ocupa. Tener en cuenta que el mínimo puede estar repetido, en cuyo caso deberán mostrarse todas las posiciones que ocupe.
#La carga de datos termina cuando se obtenga un 0 como número al azar,
#el que no deberá cargarse en la lista.

def generarLista(n):
    '''Crear una lista con números enteros entre 0 y 100.
    Recibe la cantidad a crear'''
    lista=[]
    for i in range(n):
        lista.append(random.randint(0,100))
    return lista

def valorMinimo(lista):
    '''Retorna el minimo valor de una lista.'''
    #considero primer elemento como el menor
    minimo=lista[0]
    #recorro el resto de la lista para comparar.
    for i in range(1, len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo

def mostrarPosMenor(lista, menor):
    '''Mostrar las posiciones que se encuentra el menor valor.'''
    print("El valor menor se encuentra en:")
    for i in range(len(lista)):
        if lista[i] == menor:
            print(i, end=" ")
    print()
    
def ListaPosMenor(lista, menor):
    '''Crea una lista con  las posiciones que se encuentra el menor valor.'''
    posmenores=[]
    for i in range(len(lista)):
        if lista[i] == menor:
            posmenores.append(i)
    return posmenores
    

#programa principal
cant=int(input("ingrese la cantidad a crear:"))
while cant <=0:
    cant=int(input("Error. ingrese la cantidad a crear:"))    
lista=generarLista(cant)
print(lista)
minimo = valorMinimo(lista)
print("El minimo es:",minimo)
mostrarPosMenor(lista,minimo)
lmenores=ListaPosMenor(lista,minimo)
print("posiciones del menor valor", lmenores)