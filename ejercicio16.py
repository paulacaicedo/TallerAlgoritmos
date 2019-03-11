
#EJERCICIO 16

v_inicial=float(input("Introduzca la velocidad inicial: "))
tiempo=float(input("Introduzca el tiempo: "))
aceleracion=float(input("Introduzca la aceleracion: "))

distancia=v_inicial*tiempo+1/2*(aceleracion)*pow(tiempo,2)

print("La distancia recorrida es: ",distancia)
