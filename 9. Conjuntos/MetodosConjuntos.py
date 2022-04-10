'''conjunto = {1,2,2,3,3,3,4,4,4,4,5} #No permite datos repetidos
lista =[1,2,2,3,3,3,4,4,4,4,5] #Permite datos repetidos

print(lista)
print(conjunto)'''

conjunto = {1,2,3,4,5}
print(conjunto)
#MetodoAdd - agrega al final
conjunto.add(20)
print(conjunto)

#Remove / Discard - elimina un valor
conjunto.remove(20)
conjunto.discard(1)
print(conjunto)

#Pop - elimina uno al azar
conjunto.pop()
print (conjunto)

#Update - añadir elementos
conjunto.update ([7,8,9])
print (conjunto)

#Clear - deja el conjunto vacío
conjunto.clear()
print (conjunto)