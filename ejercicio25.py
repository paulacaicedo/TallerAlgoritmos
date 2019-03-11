
#EJERCICIO 25

x=int(input("Por favor, ingrese un digito de cuatro cifras: "))

n1=x%10
n2=int((x%100)/10)
n3=int((x%1000)/100)
n4=int((x%1000)/1000)

print(str(n1)+str(n2)+str(n3)+str(n4))




