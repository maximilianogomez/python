#Se solicita simular una situación de stock actual de la siguiente forma: Ingresar por teclado los códigos de productos de cuatro dígitos, o sea, entre 1000 y 9999, hasta ingresar -1
#simulando para cada código la cantidad en stock con un número al azar entre 0 y 20.
 #Si el código ya existe en la lista se debe rechazar. Al finalizar el ingreso mostrar un listado completo con los codigos y su cantidad correspondiente por pantalla.

import random

#Funcion generarlista:
def genLista():
    #lista vacia
    listaCod = []
    listaStock = []
    #pido codigo
    cod = int(input("Ingrese un codigo de producto entre 1000 y 9999 (-1 para finalizar): "))
    while (cod < 1000 and cod != -1) or cod > 9999:
        print("El código no es válido")
        cod = int(input("Ingrese un codigo de producto entre 1000 y 9999 (-1 para finalizar): "))

    while cod != -1:
        encontrado = False
        for i in range(len(listaCod)):
            if cod == listaCod[i]:
                encontrado = True
        
        if encontrado == True :
            print("El código ya esta en la lista")           
        else:
            listaCod.append(cod)
            stock = random.randint(0,20)
            listaStock.append(stock)
        
        cod = int(input("Ingrese un codigo de producto entre 1000 y 9999 (-1 para finalizar): "))
        while (cod < 1000 and cod != -1) or cod > 9999:
            print("El código no es válido")
            cod = int(input("Ingrese un codigo de producto entre 1000 y 9999 (-1 para finalizar): "))       
    return listaCod, listaStock

#funcion informe final:
def informeF(listaStock,listaCod):
    cont = 0
    maxi = listaStock[0]
    for i in range(len(listaStock)):
        if listaStock[i] < 5:
            cont += 1
        if listaStock[i] > maxi:
            maxi = listaStock[i]
            cod = listaCod[i]
    return maxi, cod, cont
        
    
        
#Programa principal
listaCod, listaStock = genLista()
print("La lista con los codigos es: ", listaCod)
print("La lista con los stock de los producto: ", listaStock)
maximo, codigo, contador = informeF(listaStock, listaCod)
print("La cantidad maxima en stock es: ", maximo)
print("y su el código del producto es: ", codigo)
print("La cantidad de productos que poseen menos del stock minimo son: ", contador)

print("Actualizar venta")
deseaAct = str(input("¿Quiere actualizar la lista?(Si o No): "))
if deseaAct == "No" or deseaAct == "no":
    print("La cantidad maxima en stock es: ", maximo)
    print("y su el código del producto es: ", codigo)
    print("La cantidad de productos que poseen menos del stock minimo son: ", contador)
elif deseaAct == "Si" or deseaAct == "si":
    codigoProd = int(input("Ingrese un codigo de producto: "))
    while (codigoProd < 1000 and codigoProd != -1) or codigoProd > 9999:
        print("El código no es válido")
        codigoProd = int(input("Ingrese un codigo de producto entre 1000 y 9999 (-1 para finalizar): "))
    cantVendida = int(input("Ingrese la cantidad vendida: "))
    while codigoProd != -1:
        existe=False
        for i in range(len(listaCod)):
            if codigoProd == listaCod[i]:
                existe = True
                if listaStock[i]  <= cantVendida:
                    print("No existen suficientes unidades disponibles para vender")
                else:
                    listaStock[i] -= cantVendida
        if existe == False:
            listaCod.append(codigoProd)
            listaStock.append(cantVendida)
        codigoProd = int(input("Ingrese un codigo de producto: "))
        cantVendida = int(input("Ingrese la cantidad vendida: "))
    print("La lista con los codigos es: ", listaCod)
    print("La lista con los stock de los producto: ", listaStock)
else:
    print("No ingresaste una respuesta válida")
    
                
                    
                    
            