
#EJERCICIO 68

n=int(input("¿Cuantos numeros desea imprimir?: "))

positivos=0
negativos=0
pares=0
impares=0
multiOcho=0

x=int(input("Digite un numero: "))
while x<=n:
	x=int(input("Digite un numero: "))
	if x>0:
		positivos=positivos+1
	if x<0:
		negativos=negativos+1
	if x%2==0:
		pares=pares+1
	if x%2!=0:
		impares=impares+1
	if x%8==0:
		multiOcho=multiOcho+1
	x=x+1

print("Numeros positivos hay: ",positivos)
print("Numeros Negativos hay: ",negativos)
print("Numeros pares hay: ",pares)
print("Numeros Impares hay: ",impares)
print("Multiplos de Ocho hay: ",multiOcho)