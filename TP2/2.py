#ejercicio 2 Andres Lorda
n =[]
print("Seleccione 1 para ingresar alguna palabra")
print("Seleccione 0 para exit")
opcion = int(input("¿Cúal es tu opción deseada?:"))

while 1 != 0:
        
        
        if opcion == 1:
         print ( "infgrese alguna palabra")
        nombre= (input ())
        n.append (nombre)
        print("Seleccione 1 para ingresar otra palabra")
        print("Seleccione 0 para exit")     
        opcion = int(input("¿Cúal es tu opción deseada?:"))
        
        if  opcion == 0: 
                
            
           
            lista = [*n]
            lista.sort()
            
            print(lista, sep="-")
             
            print("fin")
        else:
            print ("Tenes unicamente opcion 0 y 1")