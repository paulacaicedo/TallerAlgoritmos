
#EJERCICIO 60

n=int(input("¿Cuantos numeros desea imprimir?: "))
x=1

while x<=n:
	if x%2==0:
		negativo=x*-1
		print(negativo)
	else:
		print(x)
	x=x+1