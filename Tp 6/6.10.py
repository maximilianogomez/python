#Ejercicio 10: Escribir la función comparar(a,b) que reciba como parámetros dos números enteros y devuelva 1 si el primero es mayor que el segundo
#0 si son iguales o -1 si el primero es menor que el segundo. Ejemplo: comparar(4,2) devuelve 1, y comparar(2,4) devuelve -1.

#Funciones:
def comparar(a,b):
    if a > b:
        signo = 1
    elif a < b:
        signo = -1
    else:
        signo = 0
    return signo

#Programa Ppal:
x = int(input("Ingrese un numero entero: "))
y = int(input("Ingrese otro numero entero: "))

r = comparar(x,y)

print(r)

