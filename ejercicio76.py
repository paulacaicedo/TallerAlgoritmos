
#EJERCICIO 76

n=int(input("¿Cuantos numeros desea imprimir?: "))
cantidad=0
numero=int(input("Ingrese un numero: "))
for i in range(1,n+1):
	if numero%i==0:
		print("Divisor",i)
		cantidad=cantidad+1
print("La cantidad de numeros en los que se puede dividir: ",cantidad)
