#EJERCICIO 77

usu="paula"
con="1234"
contador=0
while usu=="paula" and con=="1234":
	usuario=input("Introduzca su usuario: ")
	contrasegna=input("Introduzca su contraseña: ")
	if usuario==usu and contrasegna==con:
		print("usuario y contraseña predefinidos")
		break
	else:
		usuario!=usu and contrasegna!=con
		print("Incorrecto, Intente de nuevo")
		usuario=input("Introduzca su usuario: ")
		contrasegna=input("Introduzca su contraseña: ")
		contador = contador + 1
	if contador==3:
		print("Ha finalizado el numero de intentos")
		break
