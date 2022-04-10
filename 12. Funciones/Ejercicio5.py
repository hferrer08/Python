'''Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio'''

def cuadrado(base, altura):
    areacuadrado=base*altura
    return areacuadrado

def circulo(radio):
    areacirculo=3.1416*radio*radio
    return areacirculo

print(cuadrado(2,2))
print(circulo(3))