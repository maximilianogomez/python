#Ejercicio 8: Calcular el Máximo Común Divisor de dos enteros no negativos, basándose en las siguientes fórmulas matemáticas:
#• MCD(X,X) = X
#• MCD(X,Y) = MCD(Y,X)
#• Si X > Y => MCD(X,Y) = MCD(X-Y,Y).
#Ejemplo: MCD(40,15) devuelve 5.

#Funcion:
def mcd(a,b):
    div = 1
    mcd1 = 1
    while div <= a and div <= b:
        while a % div == 0 and b % div == 0 and div!= 1:
            a = a // div
            b = b // div
            mcd1 = mcd1 * div
        div = div + 1
    return mcd1

#Programa Ppal:
x = int(input("Ingrese un numero entero no negativo: "))
y = int(input("Ingrese otro numero entero no negativo: "))

if x < 0 or y < 0:
    print("Ingresaste un numero negativo, correr el programa nuevamente")
else:
    r = mcd(x,y)
    print("el Maximo Común Divisor es: ", r)

