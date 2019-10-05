#Ejercicio 2: Dados dos parámetros enteros A y B, obtener AB (A elevado a la B) mediante multiplicacionessucesivas, utilizando la función del ejercicio 1.

#Funcion multiplicación dada por suma:
def multSuma(a):
    i = 1
    suma = 0
    while i <= a:
        suma = suma + a
        i = i + 1
    return suma

#Programa Principal:
x = int(input("Ingrese un numero: "))

y = int(input("Ingrese la potencia por la que multiplicará: "))

resultado = 1

for i in range(y):
    resultado = resultado * (multSuma(x)//x)
    
print("El resultado de la multiplicación hecha por suma es: ", resultado)
