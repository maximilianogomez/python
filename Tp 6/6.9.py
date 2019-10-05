#Ejercicio 9: Desarrollar la función signo(n), que reciba un número entero y
#devuelva un 1, -1 o 0 según el valor recibido sea positivo,negativo o nulo.

#Funcion:
def signo(n):
    if n > 0:
        signo = 1
    elif n < 0:
        signo = -1
    else:
        signo = 0
    return signo
#Programa ppal:
a = int(input("Ingrese un numero entero: "))

r = signo(a)

print(r)