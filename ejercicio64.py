
#EJERCICIO 64

n=int(input("¿Cuantos numeros desea imprimir?: "))
x=0
suma=0

while x<=n:
	print(x)
	suma=suma+x
	x=x+1
promedio= suma/10

print("La suma es: ",suma)
print("El promedio es: ",promedio)