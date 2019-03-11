
#EJERCICIO 42

x=int(input("Introduzca un digito menor a 100.000: "))

if x>=100000:
    print("Numero menor a 100000")
if 0>=x and x<10:
    print(x,"1 digito")
if x>=10 and x<=99:
    print(x,"2 d0igitos")
if x>=100 and x<999:
    print(x,"3 digitos")
if x>=1000 and x<=9999:
    print(x, "4 digitos")
if x>=10000 and x<=99999:
    print(x, "5 digitos")


