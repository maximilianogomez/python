#Ejercicio 4: Verificar si un número es par o impar, devolviendo True o False respectivamente.

#Funcion:
def paridad(n):
    div = 1
    cant = 0
    while div <= n:
        if n % div == 0:
            cant = cant + 1
        div = div + 1
    if cant <=2:
        primo = True
    else:
        primo = False
    return primo

#Programa Principal:
n = int(input("Ingrese un numero entero : "))

resultado = paridad(n)

if resultado == True:
    print("El numero es primo")
else:
    print("El numero no es primo")
        