

#EJERCICIO 43


x=int(input("Introduzca un numero: "))
y=int(input("Introduzca un numero: "))
z=int(input("Introduzca un numero: "))


if x<y and y<z:
	print("Esta incremnetando")
elif x>y and y>z:
	print("Esta disminuyendo")
else:
	x<y and y>z
	print("Ninguna de las dos")