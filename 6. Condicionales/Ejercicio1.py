'''Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal'''

letra = input("Digite una letra: ")

if letra.lower() == "a": #para que no importe si la letra es mayuscula o minuscula
    print("Esta vocal es la a")
elif letra.lower() == "e":
    print("Esta vocal es la e")
elif letra.lower() == "i":
    print("Esta vocal es la i")
elif letra.lower() == "o":
    print("Esta vocal es la o")
elif letra.lower() == "u":
    print("Esta vocal es la u")
else:  #Esta es la condicion final por que le se pone else
    print("Esta letra no es una vocal")

    '''if letra.lower() in"aeiou": 
    print("Es una vocal")
    else:  
    print("Esta letra no es una vocal")'''