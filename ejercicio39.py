
#EJERCICIO 39

import math

print("Caulculo de raices")
a=int(input("Inserte el valor de a,por favor: "))
b=int(input("Inserte el valor de b,por favor: "))
c=int(input("Inserte el valor de c,por favor: "))

def discriminante(a,b,c):
	discrim=pow(b,2)-(4*a*c)
	return discrim

def raices(a,b,disc):
	raiz1=(-b+math.sqrt(disc))/(2*a)
	raiz2=(-b-math.sqrt(disc))/(2*a)
	return raiz1,raiz2

disc=discriminante(a,b,c)
disc_igual=(b*-1)/(2*a)

if disc<0:
	print("No existe solucion en los numeros reales")
elif disc>0:
	print("Las raices son: ")
	print (raices(a,b,disc))
else:
	disc==0
	print("Son iguales")
	print (disc_igual)