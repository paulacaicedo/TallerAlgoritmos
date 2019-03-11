
#EJERCICO 37

distancia=float(input("Introduzca la distancia a recorrer: "))
numero_dias=float(input("Introduzca los dias de estancia: "))

precio=distancia*5000

if distancia>=1000 and numero_dias>7:
    descuento=precio*15/100
    precio_total=precio-descuento
    print("Tiene descuento del 15%, el precio del pasaje es: ",precio_total)
elif distancia>=20 and distancia<1000:
    print("El precio de su pasaje es: ", precio)
else:
    distancia<20
    print("La minima distancia recorrida es de 20 km")