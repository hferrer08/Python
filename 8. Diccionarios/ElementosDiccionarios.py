diccionario = {'Nombre': 'Hubert', 'Apellido':'Ferrer', 'Estatura':1.74}
print(diccionario)
print(diccionario.keys()) #Solo imprime las llaves "Nombre, Apellido, Estatura"
print(diccionario.values()) #Solo imprime los valores "Hubert, Ferrer, 1.74"

print(diccionario["Estatura"]) #Imprime el valor de estatura
diccionario["Peso"] = "85kg" #Agregar un valor Peso
print (diccionario)
diccionario['Nombre'] = 'Hubert Antonio' #Modificar una llave
print(diccionario)