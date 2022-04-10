def valores():
    global num1 #El global sirve para que se puedan usar estas variables tanto dentro como fuera de la función, sino marcará error, se debe hacer global primero y luego asignar el valor
    global num2
    num1=110
    num2=40
    resultado = num1+num2
    return resultado


print(valores())

resta = num1-num2
print(resta)