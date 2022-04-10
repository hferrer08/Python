diccionario = {1:2,2:3,3:4}
print (diccionario)

#Metodo Pop
diccionario.pop(3) #Elimina la clave 3:4
print(diccionario)

#Metodo Clear
'''diccionario.clear() #Elimina todos los valores del diccionario
print (diccionario)'''

#Metodo get
print(diccionario.get(2)) #Muestra el valor de la clave 2:3 "El valor es 3"

#SetDefault
diccionario.setdefault(4,5) #Agrega una nueva clave y valor
print(diccionario)

#Update

diccionario2 = {4:5,5:6,6:7}
diccionario.update(diccionario2) #Agrega el diccionario2 al diccionario1
print(diccionario)

#Copy 
diccionario2.copy() #Genera una copia del diccionario
print (diccionario2)