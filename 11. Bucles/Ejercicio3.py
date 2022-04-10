'''Ejercicio 1

Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras'''

for i in range (1,11):
    print (i) #Imprime del 1 al 10

num1=(int(input("Favor digite el número 1: ")))
num2=(int(input("Favor digite el número 2: ")))

if(num2>num1):

  for i in range (num1,num2+1):
    print(i)
else:
 print("El número 2 debe ser mayor al número1")
