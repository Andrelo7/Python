#ejercicio 1 Andres Lorda
#yo lo hice de esta forma porque con while no se como sacar el numero mayor y el menor
print ("Jugemos un rato")

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
total= n1 + n2 + n3
promedio = total /3
if n1 > n2 and n1 > n3: 
    print("El numero mayor es el", n1)

elif n2 > n1 and n2 > n3:
    print ("El numero mayor es el", n2)

elif n3 > n1 and n3 > n2:
    print ("El numero mayor es el", n3)


if n1 < n2 and n1 < n3: 
    print("El numero menor es el", n1)

elif n2 < n1 and n2 < n3:
    print ("El numero menor es el", n2)

elif n3 < n1 and n3 < n2:
    print ("El numero menor es el", n3)

print("El total de todo es", total )

print ("El promedio de todo es", promedio)


