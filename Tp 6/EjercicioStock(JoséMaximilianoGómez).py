#Ejercicio stock

#Funciones:
def esPositivo(n):
    if n>0:
        return True
    else:
        return False

def fechaVal(a,b,c):
    if b > 12 or b < 0:
        i = False
        print("El mes es invalido")
    if a > 31:
        i = False
        print("El mes es invalido")
    if (b == 4 or b==6 or b==9 or b==11) and a > 30:
        i = False
        print("La fecha es invalida")
    if c % 4 == 0 and c % 400 == 0:
        i = False
        if b==2 and a != 29:
            print("La fecha es invalida")
    if i!= False:
        i = True
    return i

def vencd(a,b,c,d):
    for i in range(a,b):
        vtod = a + d
        if (b == 4 or b==6 or b==9 or b==11) and vtod > 30:
            vtod = (a + d) - 30
            vtom = b + 1
        else:
            vtod = (a + d) - 31
            vtom = b + 1
        if vtom > 12:
            vtom = 1
            vtoa = c + 1
        return vtod, vtom, vtoa
    
#Programa Principal:
x = int(input("Ingrese la cantidad de productos: "))

if esPositivo(x) == True:
    i = 0
    k = 0
    for j in range(x):
        y = int(input("Ingrese el dia: "))
        z = int(input("Ingrese el mes: "))
        w = int(input("Ingrese el año: "))
        esVal1= fechaVal(y,z,w)
        if esVal1 == False:
            print("La fecha actual es invalida")
        else:
            a = int(input("Ingrese el dia de elaboración: "))
            b = int(input("Ingrese el mes de elaboración: "))
            c = int(input("Ingrese el año de elaboración: "))
            d = int(input("¿Cuantos dias deberán transcurrir para su vencimiento?: "))
            esVal2 = fechaVal(a,b,c)
            if esVal2 == False:
                print("La fecha de elaboración no es válida")
            else:
                Vtod,Vtom,Vtoa = venc(a,b,c,d)
                if y == Vtod and z == Vtom and w == Vtoa:
                    print("El producto está vencido")
                    k += 1
                elif (z == Vtom and w == Vtoa) and (Vtod - y) <= 15:
                    print("El producto esta proximo a vencerse")
                    i += 1
    print("La cantidad de productos vencidos fueron: ", k)
    print("La cantidad de productos próximos a vencerse serán: ", i)
    
else:
    print("Ingrese un numero positivo")