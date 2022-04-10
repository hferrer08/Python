'''Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
'''

cadena1=input('Digite la primera palabra: ')
cadena2=input('Digite la segunda palabra: ')

cadena1=cadena1.lower()
cadena2=cadena2.lower()
if len(cadena1) <3 or len(cadena2)<3:
    print("Estas dos palabras no riman")
else:
 if cadena1[-3:] == cadena2[-3:]:
    print("Estas dos palabras riman")
 elif cadena1[-2:] == cadena2[-2:]:
    print("Estas dos palabran riman un poco")
 else:
    print("Estas dos palabras no riman")
