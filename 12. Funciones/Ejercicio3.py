'''Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0'''

def compararnumeros():
    num1=int(input("Digite el primer número: "))
    num2=int(input("Digite el segundo número: "))
    if (num1>num2):
        return 1
    elif (num1<num2):
        return -1
    else:
        return 0

print(compararnumeros())