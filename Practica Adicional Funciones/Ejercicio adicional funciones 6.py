#Ejercicio 6: Utilizando la función del TP6-ejercicio8, resolver:
#Ingresar números hasta -1, informar la suma absoluta de todos los números ingresados. Para lograrlo, si el número es negativo convertirlo a positivo utilizando la función signo.

#Funcion:
def mcd(a,b):
    div = 1
    aux = 0
    while div <= a and div <= b:
        if a % div == 0 and b % div == 0:
            aux = div
        div = div + 1
    return aux

#Funcion signo:
def signo(n):
    if n > 0:
        signo = 1
    elif n < 0:
        signo = -1
    else:
        signo = 0
    return signo

#Programa Principal:
nro = int(input("Ingrese un numero(-1 para finalizar): "))

suma = 0

if nro == -1:
    print("No comenzo la carga de datos")
else:
    while nro != -1:
        if signo(nro) == -1 :
            nro = nro * (-1)
            suma += nro
        else:
            suma += nro
        nro = int(input("Ingrese un numero(-1 para finalizar): "))

print("La suma absoluta de todos los numeros es: ", suma)
        
