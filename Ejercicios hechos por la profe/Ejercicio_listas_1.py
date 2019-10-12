import random
#Crear una funcion que genere una lista
#con numeros al azar entre 0 y 100 hasta
#que se genere el numero cero.
def generaAzar():
    lista=[]
    nro = random.randint(0,100)
    while nro !=0:
        lista.append(nro)
        nro = random.randint(0,100)
    return lista

def duplica(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] * 2

#programa principal
miLista=generaAzar()
print(miLista)
duplica(miLista)
print(miLista)

