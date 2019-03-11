

#EJERCICIO 65

n=int(input("¿Cuantos numeros desea imprimir?: "))

x=0
sumaPares=0
sumaImpares=0

while x<=n:
	print(x)
	if x%2==0:
		sumaPares=sumaPares+x
	else:
		sumaImpares=sumaImpares+x
	x=x+1

promedioPares=sumaPares/n
promedioImpares=sumaImpares/n
print("El promedio de los numeros pares es: ",promedioPares)
print("El promedio de los numeros impares es: ",promedioImpares)