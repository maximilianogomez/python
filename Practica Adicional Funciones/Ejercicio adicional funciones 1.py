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
nro = int(input("Ingrese un numero (-1 para finalizar): "))

i = 0
suma = 0
if nro == -1:
    print("No ingresaste ningún valor")
else:
    while nro != -1:
        if nro % 2 == 0:
            i += 1
            suma += nro
        nro = int(input("Ingrese un numero (-1 para finalizar): "))
    print("La cantidad de numeros pares ingresados fueron: ",i)
    print("La suma total de los pares fueron: ", suma)