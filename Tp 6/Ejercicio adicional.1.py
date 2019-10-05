#Ejercicio1: 
#Utilizando la función del ejercicio 4 resolver: 
#Ingresar números hasta ingresar -1. Luego informar cuantos números par se ingresaron y su suma.

#Funcion:
def paridad(n):
    if n % 2 == 0:
        resul = True
    else:
        resul = False
    return resul


#Programa principal:
cont = 0
suma = 0
nro = int(input("Ingrese un numero (-1 para finalizar): "))

while nro != -1:
    if paridad(nro) == True:
        cont+= 1
        suma = suma + nro
    nro = int(input("Ingrese u numero (-1 para finalizar): "))
print("La cantidad de numeros pares ingresados fueron: " , cont)
print("La suma de los nmeros pares fueron: ", suma)