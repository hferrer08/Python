letra = input("Digite una vocal: ")

if letra.lower() == "a": #para que no importe si la letra es mayuscula o minuscula
    print("Esta vocal es la a")
elif letra.lower() == "e":
    print("Esta vocal es la e")
elif letra.lower() == "i":
    print("Esta vocal es la i")
elif letra.lower() == "o":
    print("Esta vocal es la o")
else:  #Esta es la condicion final por que le se pone else
    print("Esta vocal es la u")