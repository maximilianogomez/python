#Ejercicio 16: Realizar una función que calcule y devuelva la sumatoria de los términos de la sucesión de Fibonacci entre dos números de término dados, los que se reciben como parámetros.

#Funcion:
def fibonacci(a,b):
    f0 = 0
    fib = 0
    f1 = 1
    i = 0
    
    while i < a :
        print(fib)
        fib = f0 + f1
        f0 = f1
        f1 = fib
        i = i + 1
    suma = 0
    while i < b:
        print(fib)
        suma = suma + fib
        fib = f0 + f1
        f0 = f1
        f1 = fib        
        i = i + 1
    return suma

#Programa ppal:

x = int(input("Desde donde quiere la serie de fibonacci: "))
y = int(input("Hasta que termino quiere la serie de fibonacci: "))

r = fibonacci(x,y)
print("suma:",r)
