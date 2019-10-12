def multiplica(a,b):
    '''multiplica a por b.'''
    sumas=0
    for cont in range(b):
        sumas = sumas + a
    return sumas

#PROGRAMA PRINCIPAL
result=multiplica(2,3)
print(result)