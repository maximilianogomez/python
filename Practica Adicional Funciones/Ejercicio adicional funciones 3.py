#Funcion multsuma:
def multSuma1(a,b):
    i = 1
    suma = 0
    while i <= b:
        suma = suma + a
        i = i + 1
    return suma
#Funcion multsuma(un valor):
def multSuma2(a):
    i = 1
    suma = 0
    while i <= a:
        suma = suma + a
        i = i + 1
    return suma
#Funcion maximo:
def maximo(a,b):
    maxi = a
    if a > b:
        maxi = a 
    elif a < b:
        maxi = b
    else:
        maxi = a
    return maxi

#Programa principal:
nro = int(input("Ingrese un numero: "))

resultado = 1

if nro < 10 or nro >99:
    print("no ingresaste un numero de dos cifras positivo ")
else:
    while nro >= 10 and nro <= 99 and nro!= -1 and nro != 0:
        dig1 = nro % 10
        nro = nro // 10
        dig2 = nro % 10
        esMaximo = maximo(dig1, dig2)
        print(maximo)
        if dig2 > dig1:
            for i in range(dig1):
                resultado *= (multSuma2(esMaximo)//esMaximo)
            print("El resultado es: ", resultado)
            resultado = 1
        else:
            for i in range(dig2):
                resultado *= (multSuma2(esMaximo)//esMaximo)
            print("El resultado es: ", resultado)
            resultado = 1
                
        nro = int(input("Ingrese un numero: "))
    
    