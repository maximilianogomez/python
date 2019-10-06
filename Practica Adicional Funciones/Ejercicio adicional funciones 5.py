#Ejercicio 5: Utilizando la función del TP6-ejercicio 7, resolver:
#Ingresar numeros hasta ingresar -1, para los positivos y el cero ir informando su factorial. Al finalizar informar cuántos números negativos se ingresaron.

#Funcion:
def fact(n):
    factorial = 1
    i = 1
    for k in range(n):
        factorial = factorial * i
        i = i + 1
    return factorial

#Programa Principal:
nro = int(input("Ingrese un numero(-1 para finalizar): "))

i = 0

if nro == -1:
    print("No se cargó ningun número")
else:
    while nro != -1:
        if nro >= 0:
            r = fact(nro)
            print("El factorial del ", nro, "es: ", r)
        else:
            i += 1
        nro = int(input("Ingrese un numero(-1 para finalizar): "))

    print("La cantidad de numeros negativos ingresados fueron: ", i)
