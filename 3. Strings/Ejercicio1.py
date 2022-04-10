cadena = "Te quiero solo como amigo"

'''• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.'''
print(len(cadena))
n=len(cadena)

#2 primeros caracteres
print(cadena[0:2])
#3 ultimos caracteres
print(cadena[-3:])
#cadena cada 2 caracteres
print(cadena[: : 2]) #EL doble : significa que saque una copia de la cadena y el 2 que vaya de 2 en 2
#cadena al reves
print(cadena[::-1]) #El doble : significa que saque una copia de la cadena y el -1 para que vaya de 1 en 1 pero con el - queda invertido
print(cadena+cadena[::-1])#la imprime normal y luego a la inversa y las suma



