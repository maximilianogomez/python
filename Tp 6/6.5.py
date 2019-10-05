#Ejercicio 5: Devolver el máximo entre dos números recibidos como parámetros.

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

#Programa Ppal:
x = int(input("Ingrese un numero entero: "))
y = int(input("Ingrese otro numero enter: "))

resultado = maximo(x,y)
        