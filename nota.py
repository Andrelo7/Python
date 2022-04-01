
#Promedio de Materias
nombre = input("Ingrese el nombre del alumno: ")
print("\nSelecione Materias: \n")
print("Presiona 1 Para Lengua")
print("Presiona 2 Para Matemática")
print("Presiona 3 Para Fisica \n")

opcion = int(input("¿Cúal es tu opción deseada?:"))

if opcion == 1:
    print("\nIngrese las notas de Lengua: \n")
    notaLengua1=float(input("ingrese nota1: "))
    notaLengua2=float(input("ingrese nota2: "))
    notaLengua3=float(input("ingrese nota3: "))
    sumaLengua=(notaLengua1 +notaLengua2 +notaLengua3)
    promedioLengua = sumaLengua/3

    print("Selecione Materias: \n")
    print("Presiona 2 Para Matematica ")
    print("Presiona 3 Para Fisica ")
    opcion2 = int(input("¿Cúal es tu opción deseada?:"))

    if opcion2 == 2:
        print("\nIngrese las notas de Matemática: \n")
        notaMate1=float(input("ingrese nota1: "))
        notaMate2=float(input("ingrese nota2: "))
        notaMate3=float(input("ingrese nota3: "))
        sumaMate=(notaMate1 +notaMate2 +notaMate3)
        promedioMate = sumaMate/3
        print("\n Solo falta ingresar una materia:")
        print("Ingrese las notas de Fisica: \n")
        notaFisica1=float(input("ingrese nota1: "))
        notaFisica2=float(input("ingrese nota2: "))
        notaFisica3=float(input("ingrese nota3: "))
        sumaFisica=(notaFisica1+notaFisica2 +notaFisica3)
        promedioFisica= sumaFisica/3
    
    elif opcion2 == 3:
        print("\nIngrese las notas de Fisica: \n")
        notaFisica1=float(input("ingrese nota1: "))
        notaFisica2=float(input("ingrese nota2: "))
        notaFisica3=float(input("ingrese nota3: "))
        sumaFisica=(notaFisica1+notaFisica2 +notaFisica3)
        promedioFisica= sumaFisica/3
        print("\nSolo falta ingresar una materia:")
        print("Ingrese las notas de Matemática: \n")
        notaMate1=float(input("ingrese nota1: "))
        notaMate2=float(input("ingrese nota2: "))
        notaMate3=float(input("ingrese nota3: "))
        sumaMate=(notaMate1 +notaMate2 +notaMate3)
        promedioMate = sumaMate/3
    else:
        print("NO ELIGIÓ UNA OPCIÓN DE LAS INDICADAS!")    
elif opcion == 2:
    print("\nIngrese las notas de Matemática: \n")
    notaMate1=float(input("ingrese nota1: "))
    notaMate2=float(input("ingrese nota2: "))
    notaMate3=float(input("ingrese nota3: "))
    sumaMate=(notaMate1 +notaMate2 +notaMate3)
    promedioMate = sumaMate/3
    print("Selecione Materias: \n")
    print("Presiona 1 Para Lengua")
    print("Presiona 3 Para Fisica\n")
    opcion3 = int(input("¿Cúal es tu opción deseada?:"))

    if opcion3 == 1:
        print("\nIngrese las notas de Lengua: \n")
        notaLengua1=float(input("ingrese nota1: "))
        notaLengua2=float(input("ingrese nota2: "))
        notaLengua3=float(input("ingrese nota3: "))
        sumaLengua=(notaLengua1 +notaLengua2 +notaLengua3)
        promedioLengua = sumaLengua/3
        print("\nSolo falta ingresar una materia:")
        print("Ingrese las notas de Fisica: \n")
        notaFisica1=float(input("ingrese nota1: "))
        notaFisica2=float(input("ingrese nota2: "))
        notaFisica3=float(input("ingrese nota3: "))
        sumaFisica=(notaFisica1+notaFisica2 +notaFisica3)
        promedioFisica= sumaFisica/3
    elif opcion3 == 3:
        print("\nIngrese las notas de Fisica: \n")
        notaFisica1=float(input("ingrese nota1: "))
        notaFisica2=float(input("ingrese nota2: "))
        notaFisica3=float(input("ingrese nota3: "))
        sumaFisica=(notaFisica1+notaFisica2 +notaFisica3)
        promedioFisica= sumaFisica/3
        print("\nSolo falta ingresar una materia:")
        print("Ingrese las notas de Lengua: \n")
        notaLengua1=float(input("ingrese nota1: "))
        notaLengua2=float(input("ingrese nota2: "))
        notaLengua3=float(input("ingrese nota3: "))
        sumaLengua=(notaLengua1 +notaLengua2 +notaLengua3)
        promedioLengua = sumaLengua/3
    else:
        print("NO ELIGIÓ UNA OPCIÓN DE LAS INDICADAS!") 
elif opcion == 3:
    print("\nIngrese las notas de Fisica: \n")
    notaFisica1=float(input("ingrese nota1: "))
    notaFisica2=float(input("ingrese nota2: "))
    notaFisica3=float(input("ingrese nota3: "))
    sumaFisica=(notaFisica1+notaFisica2 +notaFisica3)
    promedioFisica= sumaFisica/3
    print("Selecione Materias: \n")
    print("Presiona 1 Para Lengua ")
    print("Presiona 2 Para Matematica\n")
    opcion4 = int(input("¿Cúal es tu opción deseada?:"))

    if opcion4 == 1:
        print("\nIngrese las notas de Lengua: \n")
        notaLengua1=float(input("ingrese nota1: "))
        notaLengua2=float(input("ingrese nota2: "))
        notaLengua3=float(input("ingrese nota3: "))
        sumaLengua=(notaLengua1 +notaLengua2 +notaLengua3)
        promedioLengua = sumaLengua/3
        print("\nSolo falta ingresar una materia:")
        print("Ingrese las notas de Matemática: \n")
        notaMate1=float(input("ingrese nota1: "))
        notaMate2=float(input("ingrese nota2: "))
        notaMate3=float(input("ingrese nota3: "))
        sumaMate=(notaMate1 +notaMate2 +notaMate3)
        promedioMate = sumaMate/3
    elif opcion4 == 2:
        print("\nIngrese las notas de Matemática: \n")
        notaMate1=float(input("ingrese nota1: "))
        notaMate2=float(input("ingrese nota2: "))
        notaMate3=float(input("ingrese nota3: "))
        sumaMate=(notaMate1 +notaMate2 +notaMate3)
        promedioMate = sumaMate/3
        print("\nSolo falta ingresar una materia:")
        print("Ingrese las notas de Lengua: \n")
        notaLengua1=float(input("ingrese nota1: "))
        notaLengua2=float(input("ingrese nota2: "))
        notaLengua3=float(input("ingrese nota3: "))
        sumaLengua=(notaLengua1 +notaLengua2 +notaLengua3)
        promedioLengua = sumaLengua/3
    else:
        print("NO ELIGIÓ UNA OPCIÓN DE LAS INDICADAS!")   
else:
    print("NO ELIGIÓ UNA OPCIÓN DE LAS INDICADAS!")
print("\nPromedio Lengua: " , promedioLengua )
print("Promedio Matematica: " , promedioMate)
print("Promedio Fisica: " , promedioFisica)

if promedioLengua > 6:
    promociona = 1
    if promedioLengua >= 8:
      promociona = 2
    else:
      promociona =1
else:
    promociona = 0

if promedioMate >6:
    promociona2 = 1
    if promedioMate >=8:
        promociona2 = 2
    else:
        promociona2 = 1
else:
    promociona2 = 0

if promedioFisica > 6:
    promociona3 = 1
    if promedioFisica >= 8:
        promociona3 = 2
    else:
      promociona3 =1
else:
    promociona3 = 0
    
suma_de_promocion = promociona + promociona2 + promociona3

if suma_de_promocion == 6:
    print ("El alumno " , nombre, "se encuentra promocionado" )
elif suma_de_promocion == 4:
    print ("El alumno " , nombre, "se encuentra aprobado" )
elif suma_de_promocion == 5:
    print ("El alumno " , nombre, "se encuentra aprobado" )
else:
    print ("El alumno ", nombre , "se encuentra desaprobado")
    

    
print("Fin.")