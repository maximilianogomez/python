#Ejercicio 2: Calcular la suma de los números de una lista.

lista = [1,2,3,4,5]

suma = 0

for i in range(len(lista)):
    suma += lista[i]
print("La suma de sus numeros será: ", suma)