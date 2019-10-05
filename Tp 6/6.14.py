#Ejercicio 14: Obtener el dígito central de un número entero pasado como parámetro, sólo si la cantidad de dígitos es impar.
#Si la longitud fuera par devolver -1. Ejemplo: digitocentral(12345) devuelve 3, y digitocentral(123456) devuelve -1.

#Funcion:
def digitocentral(a):
    resultado = 0
    b = len(str(a))
    c = (b//2) + 1
    if len(str(a)) % 2 == 0:
            resultado = -1
    else:
        for j in range(c):
            dig = a % 10
            a = a // 10
            resultado = dig
    return resultado
    
#ProgramaPpal:
x = int(input("Ingrese un numero entero: "))

rta = digitocentral(x)

print(rta)