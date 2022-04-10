'''Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final'''

Practica1=float(input('Digite nota de practica 1: '))
Practica2=float(input('Digite nota de practica 2: '))
Practica3=float(input('Digite nota de practica 3: '))
PromPractica = (Practica1+Practica2+Practica3)/3
print("Su promedio de practicas es: \n",PromPractica)
ExParcial = float(input('Digite nota de examen parcial: '))
ExFinal = float(input('Digite nota de examen final: '))
PromFinal = (PromPractica + (2*ExParcial) + (3*ExFinal)) / 6
print("Su promedio es:\n",PromFinal)
