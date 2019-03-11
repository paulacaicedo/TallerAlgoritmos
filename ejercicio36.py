
#EJERCICIO 36

numero_1=int(input("Introduzca un primer valor: "))
numero_2=int(input("Introduzca un segundo valor: "))
numero_3=int(input("Introduzca un tercer valor: "))

resultado=numero_1+numero_2

if resultado>numero_3:
    print(resultado," es mayor a ",numero_3)
    if resultado<numero_3:
        print(resultado, " es menor a ",numero_3)
else:
    print("Son iguales")
