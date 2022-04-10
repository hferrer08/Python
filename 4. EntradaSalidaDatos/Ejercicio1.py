a=int(input("Digite variable a: ")) #Lea a
b=int(input("Digite variable b: ")) #Lea b
c=int(input("Digite variable c: ")) #Lea c
import math
x=(-b + ((((b**2)-(4*a*c)))**(1/2)))/2*a
print("La respuesta 1 es: ",x)
x2=(-b - ((((b**2)-(4*a*c)))**(1/2)))/2*a
print("La respuesta 2 es: ",x2)