#Ejercicio 13: Devolver los últimos N dígitos de un número entero pasado como parámetro.
#El valor de N también debe ser pasado como parámetro. Devolver el número completo si N es demasiado grande.
#Ejemplo: ultimosdigitos(12345,3) devuelve 345, y ultimosdigitos(12345,8) devuelve 12345.

#Funcion:
def ultimosdigitos(a,b):
    i = 1
    resultado = ""
    aux = a
    while a != 0:
        while i <= b:
            dig = a % 10
            a = a // 10
            resultado = str(dig) + resultado
            i = i + 1
        if dig == 0:
            resultado = aux
        return resultado

#ProgramaPpal:
x = int(input("Ingrese un numero entero: "))
y = int(input("que cifra desea obtener?: "))

rta = ultimosdigitos(x,y)

print(rta)