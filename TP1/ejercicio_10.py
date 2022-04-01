#ejercicio 10 Andres Lorda
import random

nombre = input("Ingrese su nombre: ")
print (f"Hola {nombre} bienvenico al juego de tu vida")
print ("Tenes que adivinar el un numero del 1 al 3 y tenes 5 intentos")
print ("Que comience el juego")

intento = input ("Ingrese un número: ")

vida = 4
a = 0
numerox = ("1", "2", "3")
random.choice (numerox)

while vida > a:
    if intento == numerox:
        break
    
    print (f"Tu vida es de: {vida}")
    vida -= 1

    print ("numero equivocado, intentalo de vuelta")
    intento = input ("Ingrese un número: ")

print ("Fin")    