#Ejercicio 4: Utilizando la función del TP6-ejercicio6, resolver:
#Desarrollar un programa para informar la cantidad de divisores que posee un numero positivo.

#Funcion:
def esmultiplo(a,b):
    if a % b == 0:
        mult = True
    else:
        mult = False
    return mult

#Programa Principal:
nro = int(input("Ingrese un numero positivo: "))

i = 1
cant = 0

if nro > 0:
    while i <= nro:
        if esmultiplo(nro,i) == True:
            cant += 1
        i += 1
    print("La cantidad de divisores que posee el numero ", nro, "son ", cant)
else:
    print("Ingresaste un numero negativo")