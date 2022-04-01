#ejercicio 6 Andres Lorda

n =[]
print("Seleccione 1 para ingresar nombre de amigo")
print("Seleccione 0 para exit")
opcion = int(input("¿Cúal es tu opción deseada?:"))

while 1 != 0:
        
        
        if opcion == 1:
         print ( "infgrese los nombres del amigo")
        nombre= (input ())
        n.append (nombre)
        print("Seleccione 1 para ingresar nombre de amigo")
        print("Seleccione 0 para exit")     
        opcion = int(input("¿Cúal es tu opción deseada?:"))
        
        if  opcion == 0: 
                
         print(*n, sep="-")
         print("fin")
