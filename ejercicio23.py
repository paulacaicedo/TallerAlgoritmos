
#EJERCICIO 23

segundos=int(input("Introduzca los segundos: "))

minutos=int(segundos/60)
minu=int(minutos%60)
seg=int(segundos%60)
horas=int(minutos/60)

print(horas," h ",minutos," min ",seg," seg")