class FabricaTelefono():
    
    def llamar(self,mensaje):   #metodo puesto que la funcion esta dentro de una class
        return mensaje

    def escucharmusica(self):
        print("Estas escuchando musica")
    
    #Atributos
    marca = "Huawei"
    color = "Negro"
    ram = 32
    almacenamiento = 128




telefono = FabricaTelefono()



print (telefono)
telefono.marca #Le asigna huawei
telefono.color
telefono.ram
print(telefono.marca) #Huawei

print(telefono.llamar("Hola, con quien hablo?")) #Desde el objeto se llama al metodo llamar
telefono.escucharmusica() #Llama el metodo por fuera de la clase por medio del objeto