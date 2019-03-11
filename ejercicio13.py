
#EJERCICIO 13

variable_a=float(input("Introduzca el primer valor: "))
variable_b=float(input("Introduzca el segundo valor: "))

print("El valor de a es: ",variable_a)
print("El valor de b es: ",variable_b)

variable_c=variable_a
variable_a=variable_b
variable_b=variable_c

print("Valores cambiados")
print("El valor de a es: ",variable_a)
print("El valor de b es: ",variable_b)
