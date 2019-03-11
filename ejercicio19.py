
#EJERCICIO 19

import math

x1=float(input("Introduzca el valor de x1: "))
x2=float(input("Introduzca el valor de x2: "))
y1=float(input("Introduzca el valor de y1: "))
y2=float(input("Introduzca el valor de y2: "))

if x1>=0 and x2>=0 and y1>=0 and y2>=0:
    d=math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
    print("La distancia entre ellos es: ",d)
else:
    print("Todos los valores tienen que ser positivos")

