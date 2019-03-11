
#EJERCICIO66

x=int(input("Ingrese un numero entero positivo: "))

while x<0:
	print("¡Numero erroneo!,Intente de nuevo")
	x=int(input("Ingrese un numero entero positivo: "))
	if x>0:
		print("Numero digitado es: ",x)

