
#Calculadora
while True: 
   try: 
        num1 = float(input("Digite el primer número para la operación: "))
        num2 = float(input("Digite el segundo número para la operación: "))
        operacion = int(input("Digite que operación quiere realizar: \n 1: suma\n 2: resta\n 3: multiplicación\n 4: división\n:"))

        def suma():
          resultado = num1+num2
          return resultado
         

        def resta():
          resultado = num1-num2
          return resultado
         

        def multiplicacion():
            resultado = num1*num2
            return resultado
           

        def division():
            resultado = num1/num2
            return resultado
            

 
        if operacion == 1: 
            print(suma())
            break
        elif operacion == 2:
            print(resta())
            break
        elif operacion == 3:
            print(multiplicacion())
            break
        elif operacion == 4:
            try:
            
              print(division())
              break
            except ZeroDivisionError:
                print("No se puede dividir entre 0")
        else:  
            print("Valor no válido, debe ser 1, 2, 3 o 4")
   except ValueError: #Si el usuario ingresa un valor que no sea int imprimirá el mensaje
              print("Ingresaste un valor erroneo, debe ser un número")