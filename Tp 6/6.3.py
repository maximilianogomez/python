#Ejercicio 3: Imprimir una columna de asteriscos, donde su altura se recibe como parámetro

#Funcion:
def asterisco(n):
    col = "*****"
    for i in range(n):
        print(col)


#Programa Principal:
n = int(input("Ingrese la altura de la columna de asteriscos: "))
asterisco(n)
    