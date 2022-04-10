'''Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas'''

lista = []
listaimpar = []
listapar=[]
cantidadn=0
numero=0

def PedirNumero():
    cantidadn=(int(input("Digite la cantidad de números que quiere ingresar a la lista: ")))
    i=0
    while i < cantidadn:
       
        numero=(int(input("Digite numero que quiere agregar a la lista: ")))
        lista.append(numero)
        i=i+1
     
    print(lista)

PedirNumero()

def OrganizarListas():
    j=0
    lista.sort() #Ordenar la lista
    while j<len(lista): #j in lista es una variante
        if lista[j]%2==0:
            par=lista[j]
            listapar.append(par)
        else:
            impar=lista[j]
            listaimpar.append(impar)
        j=j+1
       
OrganizarListas()  
print(listapar)
print(listaimpar)