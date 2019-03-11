
#EJERCICIO 33

numero_1=int(input("Introduzca un primer valor: "))
numero_2=int(input("Introduzca un segundo valor: "))

if numero_1>numero_2:
    print("El numero mayor es: ",numero_1)
    if numero_1==numero_2:
        print("Los numeros son iguales")
else:
    numero_1<numero_2
    print("El numero mayor es: ",numero_2)