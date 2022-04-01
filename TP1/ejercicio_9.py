#ejercicio 9 Andres Lorda

suma = 1
resta = 2
multiplicacion = 3
division = 4
exit = 0
print ("Que operacion quiere realizar?" )
print ("Las disponibles son: (1) suma, (2) resta, (3) multiplicacion, (4) divicion")

opcion = int(input())


while  suma != resta != multiplicacion != division:
    

    if opcion == suma:
        print("Ingrese un número")
        numero1 = input()
    
        print ("Ingrese otro numero")
    
        numero2 = input()

        
        numero1 = float (numero1)
        numero2 = float (numero2)

        print (numero1, "+", numero2, "=", numero1+numero2)
        
        print ("Que operacion quiere realizar?" )
        print ("Las disponibles son: (1) suma, (2) resta, (3) multiplicacion, (4) divicion")

        opcion = int(input())
    

    if opcion == resta:
        print("Ingrese un número")
        numero1 = input()
    
        print ("Ingrese otro numero")
    
        numero2 = input()

        
        numero1 = float (numero1)
        numero2 = float (numero2)

        print (numero1, "-", numero2, "=", numero1-numero2)

        print ("Que operacion quiere realizar?" )
        print ("Las disponibles son: (1) suma, (2) resta, (3) multiplicacion, (4) divicion")

        opcion = int(input())
    

    if opcion == multiplicacion:
        print("Ingrese un número")
        numero1 = input()
    
        print ("Ingrese otro numero")
    
        numero2 = input()

        
        numero1 = float (numero1)
        numero2 = float (numero2)

        print (numero1, "*", numero2, "=", numero1*numero2)

        print ("Que operacion quiere realizar?" )
        print ("Las disponibles son: (1) suma, (2) resta, (3) multiplicacion, (4) divicion")

        opcion = int(input())
  

    if opcion == division:
        print("Ingrese un número")
        numero1 = input()
    
        print ("Ingrese otro numero")
    
        numero2 = input()

        
        numero1 = float (numero1)
        numero2 = float (numero2)

        print (numero1, "/", numero2, "=", numero1/numero2)

        print ("Que operacion quiere realizar?" )
        print ("Las disponibles son: (1) suma, (2) resta, (3) multiplicacion, (4) divicion")

        opcion =  int(input())

