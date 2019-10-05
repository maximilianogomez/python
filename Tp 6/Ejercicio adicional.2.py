#Ejercicio2: 
#Utilizando la función del ejercicio 5: 
#ingresar N pares de números A y B. Informar el promedio de los mayores números ingresados. Ingresar N por teclado y validar que sea positivo.


#Funcion:
def maximo(a,b):
    maxi = a
    if a > b:
        print("El valor maximo es: ", maxi)
    elif a < b:
        maxi = b
        print("El valor maximo es: ", maxi)
    else:
        print("Los valores son iguales")
    return maxi

#Programa Principal:
n = int(input("Ingrese un numero entero positivo: "))

if n > 0:
    for i in range(n):
        x = int(input("Ingrese un numero: "))
        y = int(input("Ingrese un numero: "))
        maxim = maximo(x,y)
        suma = suma + maxim
        promedio = (suma/n)
    print("El promedio de los mayores ingresados serán: ", promedio)
else:
    print("El numero ingresado no es positivo ( > 0)")