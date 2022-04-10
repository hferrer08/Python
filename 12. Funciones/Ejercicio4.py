'''Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.'''



def calculariva():
  facturasiniva = float(input('Digite el valor del monto: '))
  iva = int(input('Digite el valor del iva (si lo desconoce digitar 0): '))
  if (iva>=0):
     if(iva!=0):
      
           total= facturasiniva + (facturasiniva*(iva/100))
           return total
     
     else:
      total2=facturasiniva +(facturasiniva*0.21)
      return total2
  else:
           return "El valor es negativo, favor verifique valor real del iva"

print("El total de su factura es: ",calculariva())