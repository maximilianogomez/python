#Ejercicio 7: Dado un número entero, calcular su factorial. Ejemplo: fact(4) = 4*3*2*1 = 24.

#Funcion:
def fact(n):
    factorial = 1
    i = 1
    for k in range(n):
        factorial = factorial * i
        i = i + 1
    return factorial

#Programa Principal:
x = int(input("Ingrese un numero entero: "))

r = fact(x)

print("El factorial del numero es: ", r)
    
    