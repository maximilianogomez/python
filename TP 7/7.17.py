#Ejercicio 17: Modificar el programa anterior para que las pistas brindadas por el programa no sean del tipo "es mayor" o "es menor" sino "M dígitos correctos y N dígitos aproximados".
#Se considera que un dígito es correcto cuando tanto su valor como su posición coinciden con los del número secreto, mientras que un dígito es aproximado cuando coincide el valor pero no su posición.
#Ejemplos:
#Número secreto: 5739
#• Intento 1: 1234 -> 1 correcto
#• Intento 2: 5678 -> 1 correcto y 1 aproximado
#• Intento 3: 9375 -> 4 aproximados

import random

#funcion analizar los digitos:
def analizarDig(nro,n):
    #creo una lista vacia con donde pondré los valores de los digitos del numero generado
    listadig1 = []
    #creo una lista vacia donde pondré los valores de los digitos del numero ingresado
    listadig2 = []
    while nro!= 0 and n!= 0:
        dig1 = nro % 10
        nro //= 10
        #agrego a la lista los digitos del numero generado
        listadig1.append(dig1)
        dig2 = n % 10
        n //= 10
        #agrego a la lista los digitos del numero ingresado
        listadig2.append(dig2)
    return listadig1, listadig2

#funcion ordenar las listas:
def ordenar(lista):
    i = 0
    k = len(lista) - 1
    #la idea de esta lista es ordenar el los digitos como son en la lista, ya que en la funcion anterior iban del ultimo al primero
    while i < len(lista) and k > 0:
        aux = lista[i]
        lista[i] = lista[k]
        lista[k] = aux
        i += 1
        k -= 1
    return lista

#funcion final:
def procesarDig(listadig1,listadig2):
    cont = 0
    aprox = 0
    i = 0
    k = 0
    #busco las cifras correctas
    while i < len(listadig1) and k < len(listadig2):
        if listadig2[k] == listadig1[i]:
            #si la cifra es correcta sumo 1 al contador
            cont += 1
        i += 1
        k += 1   
    for i in range(len(listadig1)):
        for k in range(len(listadig2)):
            #proceso ambas listas y si encuentro el valor,y a la vez no estan en la misma posición sumo uno al contador de aproximados
            if listadig1[i] == listadig2[k] and i != k:
                aprox += 1
    return cont, aprox
                
                
    
    
#Funcion Principal:
#creo una variable con el numero secreto
nro = random.randint(1000,9999)

#pido un numero al usuario
n = int(input("Ingrese un numero entero de cuatro cifras (-1 par finalizar): "))

#la variable cant me dirá la cantidad de intentos
cant = 0

#en esta lista almacenaré los puntajes
lista = []
#en esta lista almacenaré los nombre de las personas que sacarón dicho puntaje
nombres = []

mejor = 999999999999

#analizo el numero ingresado por el usuario hasta que devuelva uno valido
while n < 1000 or n > 9999:
    print("El numero que ingresaste es inválido")
    n = int(input("Ingrese un numero entero de cuatro cifras (-1 par finalizar): "))

while n!= -1:
    if nro < 1000 or nro > 9999:
        #pido un numero valido
        print("El numero ingresado es inválido")
        n = int(input("Ingrese un numero entero de cuatro cifras (-1 par finalizar): "))
    listadigitosnro, listadigitosn = analizarDig(nro,n)
    listadigitosnro = ordenar(listadigitosnro)
    listadigitosn = ordenar(listadigitosn)
    correctos, aproximadas = procesarDig(listadigitosnro, listadigitosn)
    if correctos != 4:
        print("La cantidad de digitos correctos de su numero ingresado fueron: ", correctos)
        print("La cantidad de digitos aproximados al numero generado: ", aproximadas)
        cant += 1
        n = int(input("Ingrese un numero entero de cuatro cifras (-1 par finalizar): "))

    if correctos == 4:
        print("Felicitaciones, usted halló el número secreto")
        print("La cantidad de intentos fueron: ", cant)
        if cant <= mejor:
            #si la cantidad de intentos es mejor que la cantidad de intentos anterior
            nombre = input("Ingrese su nombre: ")
            nombres.append(nombre)
            mejor = cant
            lista.append(mejor)
            if len(lista) > 5 and len(nombres) > 5:
                #analizo las listas y borro los primeros valores que se supone, requirieron mas intentos
                lista.pop(0)
                nombres.pop(0)
        print("Los mejores puntajes fueron: ",lista)
        print("Sus nombres respectivos fueron: : ",nombres)
        otraVez = input("Desea jugar otra vez? (Si para continuar): ")
        if otraVez == "Si" or otraVez == "si" or otraVez == "Sí" or otraVez == "sí":
            #reincio el valor secreto y las cantidades.
            nro = random.randint(1000,9999)
            cant = 0
            n = int(input("Ingrese un numero entero de cuatro cifras (-1 par finalizar): "))
        else:
            #en caso de que no se quiera jugar n vale -1 y se cierra el ciclo
            n = -1
        