'''Escribir una función que reciba una muestra de números en una lista y devuelva su medida.'''

def medida (*num):
    print(len(num))
    for i in num: #recorre la tupla
        print (i)


medida(1,2,3,5,6,4,7,8,93,5)