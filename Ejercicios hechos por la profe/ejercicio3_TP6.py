def asteriscos(cantidad):
    '''muestra por pantalla asteriscos.'''
    for cont in range(cantidad):
        print("*")
        
#programa principal
cant=int(input("Cuantos asteriscos?:"))
asteriscos(cant)