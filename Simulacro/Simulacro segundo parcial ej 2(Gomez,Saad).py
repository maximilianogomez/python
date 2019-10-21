'''Una clínica necesita un programa para atender a sus pacientes según el siguiente
criterio: Cada paciente que llega se anuncia en recepción indicando su número de socio
(validar 4 dígitos) y además le indica en recepción si viene por una urgencia (1) o con
turno (2). La clínica quiere tener una cola de atención por orden de llegada para
urgencias y otra cola de atención por orden de llegada por turno. Al finalizar el día se
ingresa -1 en el número de socio para ver todos los socios atendidos mostrando
primero los socios atendidos por urgencia y luego los socios atendidos por turno según
el orden de llegada. (2,5 ptos)
Luego se pide realizar la búsqueda de un número de socio e informar todas las veces
que fue atendido indicando si fue por turno o por urgencia y en qué orden se atendió.
(2,5 ptos)'''

#generar lista:
def generarLista():
    socios = []
    nro_socio= int(input("Ingrese su numero de socio: " ))
    while nro_socio != -1:
        while nro_socio > 9999 or nro_socio <1000:
            print("Ingresaste un numero de socio invalido")
            nro_socio=int (input("Ingrese su numero de socio :"  ))
        turno_urg= int(input(" Si viene con turno (2), si viene en urgencia (1):"  ))
        while turno_urg > 2 or turno_urg <1:
            print("Ingresaste un numero de turno invalido")
            turno_urg= int(input(" Si viene con turno (2), si viene en urgencia (1):"  ))
        socios.append(nro_socio)
        socios.append(turno_urg)
        nro_socio= int(input("Ingrese su numero de socio :"  ))
    return socios

#funcion busqueda por socio:
def busSecuencial(socios, nro_socio):
    cant = 0
    modalidad = []
    for i in range(len(socios) - 1):
        for k in range(i +1,len(socios)):
            if socios[i] == nro_socio:
                modalidad.append(socios[k])
                socios.pop(k)
                socios.pop(i)
                socios.append(-1)
                socios.append(-2)
                cant += 1
    return cant, modalidad
#funcion encontrado:
def encontrado(numeros, nro_socio):
    while nro_socio > 9999 or nro_socio <1000:
        print("Ingresaste un numero de socio invalido")
        nro_socio=int (input("Ingrese su numero de socio :"  ))
    for i in range(len(numeros)):
        if numeros[i] == nro_socio:
            z = True
            return z
    if z!= encontrado:
        z = False
    return z

#Programa principal:
numeros = generarLista()

print("La lista con el numero de socio y si tiene turno o urgencia es: ", numeros)

nro_socio=int (input("Ingrese su numero de socio :"  ))

while encontrado(numeros, nro_socio) == False:
    nro_socio=int (input("Ingrese su numero de socio :"  ))

cantidad , turno_o_urg = busSecuencial(numeros, nro_socio)
print("Cantindad de veces que se atendió ese socio:" , cantidad)
print("Modalidad de atención por orden:" , turno_o_urg)
print("Recuerde 1 es para urgencias, y 2 para turno")
    


        
        
