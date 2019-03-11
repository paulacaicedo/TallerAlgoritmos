
#EJERCICIO 30

venta=int(input("Introduzca la cantidad total de la venta: "))

iva=venta*19/100
total_venta=venta+iva
descuento=total_venta*5/100
total_venta_desc=total_venta-descuento

if iva>150000:
    print("Tiene descuento del 5% de la venta")
    print("Total venta con descuento: ",total_venta_desc)
else:
    print("No tiene descuento")
    print("Total venta con IVA: ",total_venta)
