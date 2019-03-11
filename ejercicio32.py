
#EJERCICIO 32

nota_a=float(input("Nota 1 es : "))
nota_b=float(input("Nota 2 es : "))
nota_c=float(input("Nota 3 es : "))
nota_d=float(input("Nota 4 es : "))
nota_e=float(input("Nota 5 es : "))

nota_1=(nota_a*15)/100
nota_2=(nota_b*20)/100
nota_3=(nota_c*15)/100
nota_4=(nota_d*30)/100
nota_5=(nota_e*20)/100

promedio=nota_1+nota_2+nota_3+nota_4+nota_5/5

if promedio<2.0:
    print(promedio)
    print("El estudiante no puede habilitar")
    if promedio<3.0:
        print(promedio)
        print("El estudiante reprobo la asignatura")
    else:
        promedio >= 4.5
        print(promedio)
        print("aprobo la asignatura.FELICITACIONES!!")
else:
    promedio >= 3.0
    print(promedio)
    print("El estudiante aprobo la asignatura")


