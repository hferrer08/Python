'''while True: // DIVISION ENTRE 0
     try:
          num1=(int(input("Ingresa un numero: ")))
          resultado = 100/num1
          print(resultado)
          break
     except ZeroDivisionError:
         print("No se puede dividir entre 0")'''

'''  // Si es distinto a int (String, float)
while True: #Sirve para no finalizar la ejecución sino que después del error vuelva al input
    try: #Intenta realizar la siguiente acción
           edad=int(input("Digite su edad: "))
           print('Tu edad es: ',edad)
           break
    except ValueError: #Si el usuario ingresa un valor que no sea int imprimirá el mensaje
              print("Ingresaste un valor erroneo, debe ser un número entero positivo") '''

while True: #Sirve para no finalizar la ejecución sino que después del error vuelva al input
    try: #Intenta realizar la siguiente acción
           edad=int(input("Digite su edad: "))
           print('Tu edad es: ',edad)
           
    except KeyboardInterrupt: #Si el usuario cancela con ctrl+c por accidente
        
              print("\nHas cancelado la ejecución")
              break