#ejercicio 8 Andres Lorda

import string

def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiouAEIOU":
			contador += 1
	return contador

nombre = input ("Ingrese su nombre: ")
cadena = nombre
cantidad = contar_vocales (cadena)

while cantidad < 3:
    print ("El nombre tiene que tener como minimo 3 vocales")
    input ("Ingrese su nombre con 3 vocales: ")
    break

def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiouAEIOU":
			contador += 1
	return contador

apellido = input ("Ingrese su apellido: ")
cadena = apellido
cantidad = contar_vocales (cadena)

while cantidad < 3:
    print ("El apellido tiene que tener como minimo 3 vocales")
    input ("Ingrese su apellido con 3 vocales: ")
    break

def validador_nacimiento (cts):
    if len(cts) != 4 :
        print ("Ingrese solo el año de nacimiento")
    else: 
        print ("Fecha de nacimiento ingresada con exito")
        return True
    return False

while True:
  nacimiento = input ("Ingrese su año de nacimiento:" )
  if validador_nacimiento (nacimiento):  
        break

def validador_contrasenia (cts):
    if len(cts) < 7 or len(cts) > 17:
        print ("La contrasela debe tener un minimo de 8 a un maximo de 16 caracteres")
    elif not any ([ True if c in string.punctuation else False for c in cts ]):
        print ("La contraseña debe de tener algun caracter especial")
    else: 
        print ("La contraseña a ingresada tomada con exito")
        return True
    return False

while True:
    contraseña = input ("Ingrese contraseña:" )
    if validador_contrasenia (contraseña):
        #print ("La contraseña a sido ".format (contraseña) ) 
        break

intento = input ("Ingrese la contraseña: ")
while intento != contraseña:
    print ("La contraseña es incorrecta")
    intento = input ("Intentelo otra vez: ")

print (f" Hola {nombre} {apellido}. Bienvenido de vuelta")