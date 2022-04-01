
#git config --global user.name "andreslorda"
#git config --global user.email "lorda.andrelo@gmail.com"

#for i in range(0,10):
#    print (i)
#print("\nFin")

def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiouAEIOU":
			contador += 1
	return contador

apellido = input ("Ingrese su apellido: ")
cadena = apellido
cantidad = contar_vocales (cadena)
#print (f"en la cadena {cadena} hay {cantidad} de vocales")

while cantidad < 3:
    print ("El apellido tiene que tener como minimo 3 vocales")
    input ("Ingrese su apellido con 3 vocales: ")
    break


#cantidad = contar_vocales(nombre)



