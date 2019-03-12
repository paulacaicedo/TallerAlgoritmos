
#EJERCICIO 78
menor=0
mayor=0
carga=0
nbultos=0
bultos=0
capacidad=0
cantidad=int(input("Ingrese el peso del bulto: "))
if cantidad>500:
	print("No puede exceder los 500Kg")
	cantidad=int(input("Ingrese el peso del bulto: "))
if cantidad<=500:
	if capacidad>18000:
		print("Capacidad maxima de carga")
	if capacidad<=18000:
		while capacidad<=18000:
			cantidad=int(input("Ingrese el peso del bulto: "))
			bultos=bultos+cantidad
			capacidad=capacidad+bultos
			nbultos=nbultos+1
			if cantidad<=25:
				carga=carga+cantidad*0
			if cantidad>=26 and cantidad<=300:
				carga=carga+cantidad*1500
			if cantidad>=301 and cantidad<=500:
				carga=carga+cantidad*2500
			if cantidad>mayor:
				mayor=cantidad
		promedio=bultos/nbultos
print("Numero total de bultos ingresados: ",nbultos)
print("Bulto mas pesado: ",mayor)
print("Promedio de bultos: ",promedio)
print("Total a pagar: ",carga,"pesos y ",carga*3000,"dolares")
