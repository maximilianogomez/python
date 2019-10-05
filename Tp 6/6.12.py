#Ejercicio 12: Extraer un dígito de un número entero.
#La función recibe como parámetros dos números enteros, uno será del que se extraiga el dígito y el otro indica qué cifra se desea obtener
#La cifra de la derecha se considera la número 0. Retornar el valor -1 si no existe el dígito solicitado.
#Ejemplo: extraerdigito(12345,1) devuelve 4, y extraerdigito(12345,8) devuelve -1.

#Funcion:
def extraerdigito(a,b):
    i = 0
    resultado = 0
    while a != 0:
        while i <= b:
            dig = a % 10
            a = a // 10
            resultado = dig
            i = i + 1
        if resultado == 0:
            resultado = -1
        return resultado
        
#ProgramaPpal:
x = int(input("Ingrese un numero entero: "))
y = int(input("que cifra desea obtener?: "))

rta = extraerdigito(x,y)

print(rta)