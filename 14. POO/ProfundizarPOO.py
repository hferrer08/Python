class FabricaTelefono():
    def __init__(Hubert, marca, *colores,**modelos): #'Hubert' toma la función de 'self', * tupla, ** diccionario
        Hubert.marca = marca
        Hubert.colores = colores
        Hubert.modelos = modelos

telefono = FabricaTelefono("Alcatel", "Negro","Azul","Rojo", m1=500) #Diccionario es llave = valor
print (telefono.marca)
print(telefono.colores) #Muestra la tupla colores
print(telefono.modelos) #Imprime el diccionario
telefono.memoria = 512 #Atributo temporal
print(telefono.memoria)