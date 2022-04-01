#ejercicio 4 Andres Lorda
numero1 = input("Ingrese un numero: ")
numero2 = input("Ingrese otro numero:")

numero1 = float (numero1)
numero2 = float (numero2)
if numero2 == 0:
    print ("el divisor no puede ser 0")
else:
    print (numero1, "/", numero2, "=", numero1/numero2 )
