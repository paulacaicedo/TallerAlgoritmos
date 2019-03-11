
#EJERCICIO47

import math
x1=int(input("Introduzca un numero para x1: "))
x2=int(input("Introduzca un numero para x2: "))
y1=int(input("Introduzca un numero para y1: "))
y2=int(input("Introduzca un numero para y2: "))
radio_tierra=int(input("Introduzca el radio: "))

distancia=radio_tierra*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))

print("La distancia es: ",distancia)