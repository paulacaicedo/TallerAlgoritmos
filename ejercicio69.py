
#EJERCICIO 69

pares=0
num5=0
i=1

while i>0:
	print(i)
	i=i+1
	if i%2==0:
		pares=pares+1
	if i%5==0:
		num5=num5+1
	if pares==100:
		break
	if num5==80:
		break

print("Numeros leidos: ",i)
print("Numeros pares: ",pares)
print("Numeros 5: ",num5)