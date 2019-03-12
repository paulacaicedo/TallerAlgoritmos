
#EJERCICIO 80

n=int(input("Por favor ingrese el numero de filas: "))
for i in range(n+1):
	for j in range(0,i):
		i=i+j
		print(end=str(i))
	print("")