#ejercicio 5 Andres Lorda
print ("arroje un numero")
numero1 = input ()
print ("arroje un numero más")
numero2 = input ()
print ("arroje un ultimo numero")
numero3 = input ()

numero1 = float (numero1)
numero2 = float (numero2)
numero3 = float (numero3)
#print (list.sort (numero1, numero2, numero3))

if numero1 > numero2 and numero1 > numero3: 
    print(f"El numero mayor es el {numero1}")

if numero2 > numero1 and numero2 > numero3:
    print (f"El numero mayor es el {numero2}")

if numero3 > numero1 and numero3 > numero2:
    print (f"El numero mayor es el {numero3}")