#Ejercicio 7: Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del año, con el propósito de ofrecerles un agasajo especial en su día.
#Desarrollar un programa que lea el número de legajo y fecha de nacimiento (día, mes y año) de cada uno de los alumnos que concurren a dicha escuela.
#La carga finaliza con un número de legajo igual a -1.
#Emitir un informe donde aparezca -mes por mes- cuántos alumnos cumplen años a lo largo del año.
#Imprimir también una leyenda que indique cuál es el mes con mayor cantidad de cumpleaños.

#Funcion generar lista:
def genLista():
    #creo una lista en blanco con los 12 meses
    lista = [0, 0, 0, 0 ,0 , 0 ,0 ,0 ,0 ,0, 0, 0]
    #Introduzco los legajos
    leg = int(input("Ingrese el numero de legajo(-1 para terminar): "))
    if leg == -1:
        #no se cargo nada todavia
        print("No se empezaron a cargar datos")
    else:
        while leg != -1:
            #Ingreso las fechas
            print("Ingrese la fecha de nacimiento")
            dia = int(input("Ingrese el dia de nacimiento: "))
            mes = int(input("Ingrese el mes de nacimiento: "))
            año = int(input("Ingrese el año de nacimiento: "))
            lista[mes - 1] += 1
            leg = int(input("Ingrese el numero de legajo(-1 para terminar): "))
        return lista

#Funcion comparar valores:
def maximovalores(lista):
    max = 0
    for i in range(len(lista)):
        if lista[i] >= max:
            max = lista[i]
            k = i
    return max, k
            

#Programa Principal:
lista = genLista()
print(lista)
mayor, mes = maximovalores(lista)
#informe:
for i in range(len(lista)):
    print("La cantidad de alumnos que cumplen en el mes", i + 1, " son: ", lista[i])
print("El mes con mayor cantidad de cumpleaños fue el mes: ", mes + 1, "con ", mayor)
    
