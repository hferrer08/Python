'''class FabricaTelefono():
      marca = "Samsung"

      def ElaborarHuawei(self):
              self.marca = "Huawei" #Globalizar el atributo en todo el programa


telefono = FabricaTelefono()

telefono.ElaborarHuawei()
print(telefono.marca)'''

class FabricaTelefono():
    def __init__(self, marca, color): #Se ejecuta cuando se crea un objeto automaticamente sin llamarlo, es de python
      #Se agregan los atributos automaticamente cuando se crea el objeto sin necesidad de llamarlo
       self.marca = marca
       self.color = color



telefono = FabricaTelefono('Huawei', 'Negro') #Por medio del init le brindo los atributos al momento de crearlo
print (telefono.marca)
print (telefono.color)
