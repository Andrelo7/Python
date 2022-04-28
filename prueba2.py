n =[]
print("Seleccione 1 para ingresar algun número")
print("Seleccione 0 para exit")
opcion = int(input("¿Cúal es tu opción deseada?:"))

while 1 != 0:
        
        
        if opcion == 1:
         print ( "infgrese algun número")
        nombre= (input ())
        n.append (nombre)
        print("Seleccione 1 para ingresar otra palabra")
        print("Seleccione 0 para exit")     
        opcion = int(input("¿Cúal es tu opción deseada?: "))
        
        if  opcion == 0: 
                
            
           
            lista = [*n]
            #lista.sort()
            menor_numero = lista [0]
            mayor_numero = lista [0]
            for x in lista:
                if (menor_numero > x):
                    menor_numero = x
            print ("el numero menor es el", menor_numero)

            for x in lista:
                if (mayor_numero < x):
                    mayor_numero = x
            print ("el mayor es el", mayor_numero)
            
            total= None
                

            print("fin")
        else:
            print ("Tenes unicamente opcion 0 y 1")



