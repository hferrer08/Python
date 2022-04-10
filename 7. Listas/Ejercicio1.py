'''En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]

'''

lista = [20, 50, "Curso", 'Python', 3.14]
print("Estos son los valores actuales de la lista: ",lista)
Dato1=input("Digite primer dato a sustituir en la lista: ")
lista[0]=(Dato1)
Dato2=input("Digite segundo valor a sustituir en la lista: ")
lista[1]=(Dato2)
print("El nuevo valor de la lista es: ",lista)
