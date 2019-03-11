
#EJERCICIO 34

numero_1=int(input("Introduzca un primer valor: "))
numero_2=int(input("Introduzca un segundo valor: "))
numero_3=int(input("Introduzca un tercer valor: "))

if numero_1>numero_2 and numero_1>numero_3:
    print("El numero mayor es: ",numero_1)
    if numero_2>numero_1 and numero_2>numero_1:
        print("El numero mayor es: ",numero_2)
        if numero_3>numero_1 and numero_3>numero_2:
            print("El numero mayor es: ",numero_3)
else:
    print("Todos son iguales")
