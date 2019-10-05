#Ejercicio 1: Dados dos parámetros numéricos, calcular y devolver el resultado de la multiplicación de ambos utilizando sólo sumas

#Funcion:
def multSuma(a,b):
    i = 1
    suma = 0
    while i <= b:
        suma = suma + a
        i = i + 1
    return suma

#Programa Principal:
x = int(input("Ingrese un numero: "))

y = int(input("Ingrese otro numero: "))

resultado = multSuma(x,y)

print("El resultado de la multiplicación hecha por suma es: ", resultado)