
#EJERCICIO 17

masa=float(input("Introduzca la masa: "))
velocidad_luz=float(input("Introduzca la velocidad de la luz: "))

masa_gramos=masa*1000
energia=masa_gramos*pow(velocidad_luz,2)

print("La energia es: ",energia, " jules ")
