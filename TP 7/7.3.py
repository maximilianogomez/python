#Ejercicio 3: Determinar si una lista es capicúa.

#Funcion determinar si es capicúa:
def esCap():
    k = 1
    lista = [1 , 6 ,5, 6,  1]
    for i in range((len(lista)//2)):
        if lista[i] == lista[len(lista) - k]:
            cap = True
        else:
            cap = False
        k += 1
    return cap

#Funcion principal:



if esCap() == False:
    print("La lista no es capicúa")
else:
    print("La lista es capicúa")
