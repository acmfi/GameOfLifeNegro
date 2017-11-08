def verCel(b):                           #ver estado de la célula
    if b:
        return 'o'                       #True = célula viva
    else:
        return '·'                       #False = célula muerta

def dibFila(fila):                       #dibujar una fila basada en una lista de booleanos
    res=[]
    for b in fila:
        res.append(verCel(b))            #añade los valores booleanos del principio a la lista
    return res                           #devuelve una lista con los valores establecidos al principio

def dibMatriz(mat):                      #dibujar una matriz basada en listas de booleanos
    res=[]
    for b in mat:
        res.append(print(dibFila(b)))    #añade los valores booleanos segun los valores que tengan las filas introducidas   
    return res                           #devuelve una matriz con los valores del principio
