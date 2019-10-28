'''Generar una lista de N elementos de números creados al azar entre 1 y 1000.
Validar N sea positivo (1 pto) Luego Se pide:
a) Ingresar un dato por teclado, hasta que No exista en la lista.
Utilizar una función para determinar si el número se encuentra en la lista.
Insertar el elemento en la primer posicion de la lista, desplazando el resto una posición. (2 ptos) 

b) Mediante una función, para cada ocurrencia del menor número, intercambiarlo con el elemento que lo antecede.
Si se encuentra en la primera posición, no realizar intercambio.
Informar cuántos intercambios se realizaron. (2 ptos) Mostrar por pantalla antes y despues de modificar la lista. '''
 
import random
 
#funcion generarlista
def genLista():
    lista = []
    n = int(input("Ingrese la cantidad de elementos que tendrá la lista: "))
    while n < 0:
        print("Introdujó un valor que no es positivo (<0)")
        n = int(input("Ingrese la cantidad de elementos que tendrá la lista: "))
    for i in range(n):
        num = random.randint(1,1000)
        lista.append(num)
    return lista
#buscar en lista numero
def buscarNumero(numero, lista):
    encontrado = 0
    for i in range(len(lista)):
        if numero == lista[i]:
            #se encontró el valor en la lista
            encontrado = 1
    return encontrado
#insertar numero
def insertarNum(numero, lista):
    nuevaLista = []
    nuevaLista.append(numero)
    for i in range(len(lista)):
        nuevaLista.append(lista[i])
    return nuevaLista

#Hallar menor numero
def hallarMenor(lista):
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor
#Hallar la ocurrencia de ese menor
def ocurrenciaMenor(lista, menor):
    cant = 0
    for i in range(len(lista)):
        if lista[i] == menor and i!= 0:
            aux = lista[i]
            lista[i] = lista[i - 1]
            lista[i - 1] = aux
            cant += 1
    return lista, cant
        


#Programa Principal
numeros = genLista()
#item a 
print("La lista actual sin insertar el numero es : ", numeros)
nro = int(input("Ingrese el numero a buscar en la lista: "))
while buscarNumero(nro,numeros) == 1:
    print("El numero que busca se encuentra en la lista")
    nro = int(input("Ingrese el numero a buscar en la lista: "))
numeros = insertarNum(nro, numeros)
print("La lista con el numero insertado al principio es: ", numeros)
#item b

menor = hallarMenor(numeros)
print("El menor numero de la lista es: ", menor)
lista , contador = ocurrenciaMenor(numeros, menor)
print("La nueva lista con los valores cambiados es : ", lista)
print("La cantidad de veces que cambió su menor es: ", contador)

    
    
            
        
    
    