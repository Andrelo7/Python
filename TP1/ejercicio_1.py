#ejercicio1 Amdres Lorda
nombre = input("Ingrese el nombre del alumno: ")
print("Igrese las materia que se esta cursando")
materia1 = input ("Nombre de la primera materia: ")
materia2 = input ("Nombre de la segunda materia: ")
materia3 = input ("Nombre de la tercera materia: ")
materia4 = input ("Nombre de la cuarta materia: ")

print (f"Ahora vamos a cargarle las notas de las materias, (1) para {materia1}, (2) para {materia2}, (3) para {materia3}, (4) para {materia4} ") 
opcion = int(input("Cual es tu opcion?: "))

while 1 != 2 != 3 !=4 != 0:
    
    if opcion == 1:
        print (f"Ingrese las nota de {materia1}")
        nota1materia1 = float (input("Ingrese la primera nota: "))
        nota2materia1 = float (input("Ingrese la segunda nota: "))
        nota3materia1 = float (input("Ingrese la ultima nota: "))
        sumamateria1 = ( nota1materia1+nota2materia1+nota3materia1 )
        promediomateria1 = sumamateria1/3
    
        print("Seleccione la siguiente materia")
        print (f" (2) para {materia2}, (3) para {materia3}, (4) para {materia4}, (0) para salir ")
        opcion = int(input("Cual es tu opcion?: "))
    

    if opcion == 2:
        print (f"Ingrese las nota de {materia2}")
        nota1materia2 = float (input("Ingrese la primera nota: "))
        nota2materia2 = float (input("Ingrese la segunda nota: "))
        nota3materia2 = float (input("Ingrese la ultima nota: "))
        sumamateria2 = ( nota1materia2+nota2materia2+nota3materia2 )
        promediomateria2 = sumamateria2/3

        print("Seleccione la siguiente materia")
        print (f" (1) para {materia1}, (3) para {materia3}, (4) para {materia4}, (0) para salir ")
        opcion = int(input("Cual es tu opcion?: "))

    if opcion == 3:
        print (f"Ingrese las nota de {materia3}")
        nota1materia3 = float (input("Ingrese la primera nota: "))
        nota2materia3 = float (input("Ingrese la segunda nota: "))
        nota3materia3 = float (input("Ingrese la ultima nota: "))
        sumamateria3 = ( nota1materia3+nota2materia3+nota3materia3 )
        promediomateria3 = sumamateria3/3

        print("Seleccione la siguiente materia")
        print (f" (1) para {materia1}, (2) para {materia2}, (4) para {materia4}, (0) para salir ")
        opcion = int(input("Cual es tu opcion?: "))

    if opcion == 4:
        nota1materia4 = float (input("Ingrese la primera nota: "))
        nota2materia4 = float (input("Ingrese la segunda nota: "))
        nota3materia4 = float (input("Ingrese la ultima nota: "))
        sumamateria4 = ( nota1materia4+nota2materia4+nota3materia4 )
        promediomateria4 = sumamateria4/3

        print("Seleccione la siguiente materia")
        print (f" (1) para {materia1}, (2) para {materia2}, (3) para {materia3}, (0) para salir ")
        opcion = int(input("Cual es tu opcion?: "))

    if opcion == 0:
        print (f"El promedio de la materia {materia1} es de {promediomateria1}") 
    print (f"El promedio de la materia {materia2} es de {promediomateria2}") 
    print (f"El promedio de la materia {materia3} es de {promediomateria3}") 
    print (f"El promedio de la materia {materia4} es de {promediomateria4}")    

    print("Fin")