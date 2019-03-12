
#EJERCICIO 81

n=int(input("Por favor ingrese el numero de filas: "))
for i in range(n,0,-1):
	for j in range(0,i,1):
		print(end="*")
	print("")
