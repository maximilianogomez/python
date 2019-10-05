#Ejercicio 6: Devolver True si el número entero recibido como primer parámetro es múltiplo del segundo, o False en caso contrario.
#Ejemplo: esmultiplo(40,8) devuelve True y esmultiplo(50,3) devuelve False.

#Funcion:
def esmultiplo(a,b):
    if a % b == 0:
        mult = True
    else:
        mult = False
    return mult

#Programa ppal:
x = int(input("Ingrese un numero entero: "))
y = int(input("Ingrese otro numero entero: "))

r = esmultiplo(x,y)

print(r)