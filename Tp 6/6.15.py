#Ejercicio 15: Escribir una función que reciba como parámetros dos números enteros y devuelva la concatenación de ambos. Por ejemplo concatenar(123,456) devuelve 123456.

#Funcion:
def concatenar(a,b):
    resultado = ""
    resultado = str(a) + str(b)
    return resultado

#Programa Ppal:
x = int(input("Ingrese un numero entero: "))
y = int(input("Ingrese otro numero entero: "))

r = concatenar(x,y)

print("La concatenación de ambos números será: ", r)