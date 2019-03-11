
#EJERCICIO 38

print("Programa de año bisiesto")

agno=int(input("Introduce agno: "))

if agno%4==0 or agno%400==0 and agno%100!=0:
	print("Es bisiesto")
elif agno%100==0 and agno%400!=0:
	print("No es bisiesto")
else:
	print("No es bisiesto")