#Ejercicio 1: Escribir una función para ingresar desde el teclado una serie de números entre 1 y 20 y guardarlos en una lista.
#En caso de ingresar un valor fuera de rango el programa mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la carga se deberá ingresar -1.
#La función no recibe ningún parámetro, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como valor de retorno.  
 
#En los siguientes ejercicios utilice la función del ejercicio 1 para ingresar datos en una lista y:

#Funcion:
def GenerarLista():
    #creamos lista vacia
    lista = []
    #pedimos numero
    nro = int(input("Ingresar un numero entre 1 y 20: "))
    while nro != -1:
        #procesar dato
        if nro >= 1 and nro <= 20:
            #agregamos el numero entre 1 y 20
            lista.append(nro)
        else:
            print("Numero no válido")
        nro = int(input("Ingresar un numero entre 1 y 20: "))
    return lista

#Programa Principal:


#creo una lista usando la funcion generarLista
numeros = GenerarLista()
#muestro la lista por pantalla
print("La lista es :", numeros)

#Cantidad de elemntos de la lista:
print("La cantidad de elementos es: ", len(numeros))
#Mostrar la suma de todos los elementos de la lista:
suma = 0
for i in range(len(numeros)):
    suma += numeros[i]
print("La suma de sus numeros será: ", suma)
#Suma de ciclos while:
suma = 0
i = 0
while i < len(numeros):
    suma+= numeros[i]
    i+= 1
print("La suma de sus numeros hecho con while: ", suma)
    
    