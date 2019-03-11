
#EJERCICIO 67

n=int(input("¿Cuantos numeros desea imprimir?: "))

x=0
mayor100=0
menor100=0

while x<=n:
	print(x)
	if x>100:
		mayor100=mayor100+1
	else:
		menor100=menor100+1
	x=x+1

print("Numeros mayores a 100: ",mayor100)
print("Numeros menores a 100: ",menor100)
