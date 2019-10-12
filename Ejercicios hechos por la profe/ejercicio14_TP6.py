def contarDigitos(nro):
    '''cuenta la cantidad de digitos.'''
    cont=0
    while nro > 0:
        nro = nro //10
        cont = cont + 1
    return cont

def digitoCentral(nro):
    '''Retorna el digito central.'''
    #primero cuento los digitos
    digitos = contarDigitos(nro)
    if digitos %2 ==0:
        unDigito =-1
    else:
        #calculo la mitad
        mitad = digitos //2
        cont=0
        while cont <= mitad:
            unDigito= nro %10
            nro = nro //10
            cont = cont + 1
    return unDigito    
    
    

#programa principal
num=int(input("ingrese un numero:"))
print("El digito central es",digitoCentral(num))