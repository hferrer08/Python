'''Ejercicio 1

Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero'''

num = int(input("Digite un número para saber su tabla de multiplicar: "))
i=1
while i<=10:
    resultado = num*i
    print("",num,"X",i,"=",resultado)
    i = i+1