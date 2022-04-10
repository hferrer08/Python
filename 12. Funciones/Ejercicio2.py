'''Escribir una función que reciba un número entero positivo y devuelva su factorial.'''


numero = (int(input("Digite un numero para realizar su factorial: ")))

def factorial():
    i=1
    n=1
    while i <= numero:
            n=n*i
            i=i+1
    print(n)

factorial()

'''from math import factorial
factorial(num) y no es necesario hacer bucle'''