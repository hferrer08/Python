while True: #Sirve para no finalizar la ejecución sino que después del error vuelva al input
    try: #Intenta realizar la siguiente acción
           edad=int(input("Digite su edad: "))
           print('Tu edad es: ',edad)
           break
    except: #Si el usuario ingresa un valor que no sea int imprimirá el mensaje
              print("Ingresaste un valor erroneo, debe ser un número entero positivo")
    finally:
               print("La ejecución ha finalizado") #se ejecuta al final en cualquier caso