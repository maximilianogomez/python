'''2) Un club desea llevar registro de los socios que visitan el club por día.
Para ello, desea
ingresar el número de socio de cantidad impar de dígitos y la cantidad de horas de permanencia en el club (considerar que no puede superar las 24 horas),
se ingresa un codigo -1 como fin de carga. (1 pto.) 
 
Se pide informar:

a) Ordenar de menor a mayor por el dígito central del número de socio. (2 ptos) 
 
b) Para cada socio, informar cuántas veces ingresó al club y la cantidad total de horas que permaneció en el club, en formato de (dias, horas, minutos).
En el informe No se debe repetir el número de socio.
Desarrollar mediante funciónes. (resolver sin modificar el orden de la lista) ( 2 pto)'''

#funcion analizar digitos
def analisisDig(nro):
    cont = 0
    while nro!= 0:
        dig = nro % 10
        nro //= 10
        cont += 1
    return cont

def analisis2Dig(nro):
    cont = 0
    aux = nro
    while nro!= 0:
        dig = nro % 10
        nro //= 10
        cont += 1
    central = (cont//2) + 1
    for i in range(central):
        dig = aux % 10
        aux = aux // 10
    return dig
    
#funcion generarlista
def genLista():
    listasocio = []
    listahoras = []
    nro_socio = int(input("Ingrese el numero de socio(debe tener una cantidad impar de digitos, -1 para finalizar): "))
    #verificación
    while nro_socio != -1:
        while analisisDig(nro_socio) % 2 == 0:
            print("Ingreso una cantidad impar de digitos para el numero de socio")
            nro_socio = int(input("Ingrese el numero de socio(debe tener una cantidad impar de digitos, -1 para finalizar): "))
        listasocio.append(nro_socio)
        canthoras = float(input("Ingrese la cantidad de horas que permanecerá el socio: "))
        while canthoras > 24:
            print("Ingreso una cantidad de horas de permanencia mayor a 24")
            canthoras = float(input("Ingrese la cantidad de horas que permanecerá el socio: "))
        listahoras.append(canthoras)
        nro_socio = int(input("Ingrese el numero de socio(debe tener una cantidad impar de digitos, -1 para finalizar): "))
    return listasocio, listahoras

#funcion digitocentral:
def digitoCentral(listasocio):
    listadig = []
    for i in range(len(listasocio)):
        cantdig = analisis2Dig(listasocio[i])
        listadig.append(cantdig)
    print("desordenada:", listadig)
    for i in range(len(listadig) - 1):
        for k in range(i + 1, len(listadig)):
            if listadig[i] > listadig[k]:
                aux1 = listadig[i]
                listadig[i] = listadig[k]
                listadig[k] = aux1
                aux2 = listasocio[i]
                listasocio[i] = listasocio[k]
                listasocio[k] = aux2
    return listadig, listasocio
        
#Programa principal:
listasocio, listahoras = genLista()
print(listasocio)
print(listahoras)

#item a
listadig, listasocioact= digitoCentral(listasocio)
print(listadig)
print(listasocioact)
        
        
        
        