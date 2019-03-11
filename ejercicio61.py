
#EJERCICIO 61

n=int(input("Ingrese un numero: "))
m=int(input("Ingrese un numero mayor al anterior: "))

if n>m:
	print("SE LE PIDIO QUE EL SEGUNDO NUMERO FUERA MAYOR!!")
else:
	while n<=m:
		print("Numero Natural: ",n)
		n=n+1