#ejercicio 3 Andres Lorda
import random
print ("BIENVENIDO A PIEDRA, PAPEL O TIJERAAA")
print ("JUGAS CONTRA LA INTELIGENCIA MAS GRANDE DEL PLANETA!!!!")
print ("El prmero que llegue a tres gana")
U = 0
P = 0
while True :
    
    aleatorio = random.randrange(0, 3)
    pc = ""
    print("1, Piedra")
    print ("2, Papel")
    print ("3, Tijera")
    opcion = int(input("Elige tu opcion: "))

    if opcion == 1:
        usuario = "Piedra"
    elif opcion ==2:
        usuario = "Papel"
    elif opcion ==3:
        usuario = "Tijera"
    print ("Has elejido", usuario)

    if aleatorio ==0:
        pc = "Piedra"
    elif aleatorio ==1:
        pc = "Papel"
    elif aleatorio ==2:
        pc = "Tijera"
    print ("La compu elijio ", pc)
    print ("...")
    if pc == "Piedra" and usuario == "Papel":
        print ("Ganaste!!! Se te sumo un punto :D")
        U +=1
    elif pc == "Papel" and usuario == "Tijera":
        print ("Ganaste!!! Se te sumo un punto:D")
        U +=1
    elif pc == "Tijera" and usuario == "Piedra":
        print ("Ganaste!!! Se te sumo un punto :D")
        U +=1
    elif pc == usuario:
        print ("Empate!! WOW, Nadie sumo un puntos")
    elif pc == "Piedra" and usuario == "Tijera":
        print ("Perdiste, La Maquina sumo un punto :(")
        P +=1
    elif pc == "Papel" and usuario == "Piedra":
        print ("Perdiste La Maquina sumo un punto :(")
        P +=1
    elif pc == "Tijera" and usuario == "Papel":
        print ("Perdiste La Maquina sumo un punto :(")
        P +=1
    
    if P==3:
        print ("La Maquina llego a 3 puntos")
        print ("PERDISTE :´´´´[")
        break
    elif U==3:
        print ("Has llegado a 3 puntos!!!!")
        print ("GANASTE!!!")
        break    
