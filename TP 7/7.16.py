#Ejercicio 16: Desarrollar un programa que genere un número entero al azar de cuatro cifras y proponerle al usuario que lo descubra, ingresando valores repetidamente hasta hallarlo.
#En cada intento el programa mostrará mensajes indicando si el número ingresado es mayor o menor que el valor secreto. Permitir que el usuario abandone al ingresar -1.
#Informar la cantidad de intentos realizada al terminar el juego, haciendo que el usuario ingrese su nombre si mejoró la mejor marca de intentos obtenida hasta el momento.
#Luego mostrar la lista de los 5 mejores puntajes y preguntar si se desea jugar otra vez, reiniciando el juego en caso afirmativo

import random

#creo una variable con el numero secreto
nro = random.randint(1000,9999)

#pido un numero al usuario
n = int(input("Ingrese un numero entero de cuatro cifras (-1 par finalizar): "))

cant = 0

lista = []

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
    if nro > n:
        print("El numero secreto es mayor que el numero ingresado")
        cant += 1
        n = int(input("Ingrese un numero entero de cuatro cifras (-1 par finalizar): "))
    elif nro < n:
        print("El numero secreto es menor que el numero ingresado")
        cant += 1
        n = int(input("Ingrese un numero entero de cuatro cifras (-1 par finalizar): "))
    else:
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
        




        