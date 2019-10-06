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
n = int(input("ingrese la cantidad de pares que ingresará : "))

suma = 0
cont = 0
if n > 0:
    for i in range(n):
        a = int(input("Ingrese un numero a : "))
        b = int(input("Ingrese un numero b : "))
        cMaximo = maximo(a,b)
        suma += cMaximo
        cont += 1
        prom = suma/cont
    print("El promedio es: ", prom)
else:
    print("n no es positivo")