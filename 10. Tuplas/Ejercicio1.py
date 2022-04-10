'''Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla'''

tupla=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
numero = (int(input("Digite el número de mes que quiere saber: ")))
print("El mes que desea saber es: ",tupla[numero-1])