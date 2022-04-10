'''Ejercicio 2

Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares'''

num1=(int(input("Favor digite el número 1: ")))
num2=(int(input("Favor digite el número 2: ")))

if(num2>num1):

  for i in range (num1,num2+1):
      if(i%2!=0):
         print(i)
else:
 print("El número 2 debe ser mayor al número1")