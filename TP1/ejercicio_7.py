#ejercicio 7 Andres Lorda
print("Por favor ingrese su nombre")
nombre = input()
print("Por favor ingrese su apellido")
apellido = input()
print ("Por favor ingrese su edad")
edad = int (input())
print ("Por favor escriba cuanto dinero tiene en el bolsillo")
dinero = int (input())
print ("En una escala de 1 al 10, ingrese su hambre")
hambre = int (input())

if edad < 35:
    print (f"Hola {nombre}, Eres una persona joven ya que tu edad es de {edad}")

if edad > 34 and dinero > 500 and hambre > 5:
    print (f"Hola {nombre} {apellido} ¿Hoy hay asado?")

if hambre < 7 or dinero < 100 and edad < 18:
    print (f"Hola {nombre} {apellido} ¿Vamos a comer a lo de tus padres?")
