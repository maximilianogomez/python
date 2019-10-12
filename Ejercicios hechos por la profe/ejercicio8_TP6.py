def calculaMCD(x,y):
    '''calcula el MCD de x e y.'''
    while x !=y:
        if x > y:
            x = x -y
        else:
            y = y -x    
    return x
    
#programa principal
x = int(input("ingrese un numero:"))
y = int(input("ingrese otro numero:"))
print("El MCD es:",calculaMCD(x,y))


