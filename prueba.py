from pathlib import Path
import os

carpeta_principal = ("Pokemones")
sub_carpeta1 = ("Fuego")
sub_carpeta2 = ("Electrico")
sub_carpeta3 = ("Agua")

Generar_carpeta = Path(carpeta_principal+"/"+sub_carpeta1)
Generar_carpeta.mkdir(parents=True,exist_ok=True)

Generar_carpeta = Path(carpeta_principal+"/"+sub_carpeta2)
Generar_carpeta.mkdir(parents=True,exist_ok=True)

Generar_carpeta = Path(carpeta_principal+"/"+sub_carpeta3)
Generar_carpeta.mkdir(parents=True,exist_ok=True)

ArchivoLibro = open("Pokemones/Fuego/Tipo Fuego.txt", "w")
ArchivoLibro.write("Su forma base CHARMANDER a nivel 16 evoluciona a CHARMELEON a nivel 36 evoluciona a CHARICARD"+"\n\n")
ArchivoLibro.write("Su forma base CYNDAQUIL a nivel 16 evoluciona a QUILAVA a nivel 36 evoluciona a TYPHLOSION"+"\n\n")
ArchivoLibro.write("Su forma base CHIMCHAR a nivel 16 evoluciona a MONFERNO a nivel 36 evoluciona a INFERNAPE")
ArchivoLibro.close()

ArchivoLibro = open("Pokemones/Agua/Tipo Agua.txt", "w")
ArchivoLibro.write("Su forma base SQUIRTLE a nivel 16 evoluciona a WARTORTLE a nivel 36 evoluciona a BLASTOISE"+"\n\n")
ArchivoLibro.write("Su forma base TOTODILE a nivel 16 evoluciona a CROCONAW a nivel 36 evoluciona a FERALIGATR"+"\n\n")
ArchivoLibro.write("Su forma base PIPLUP a nivel 16 evoluciona a PRINPLUP a nivel 36 evoluciona a EMPOLEON")
ArchivoLibro.close()

ArchivoLibro = open("Pokemones/Electrico/Tipo Electrico.txt", "w")
ArchivoLibro.write("Su forma base SHINX a nivel 15 evoluciona a LUXIO a nivel 30 evoluciona a LUXRAY"+"\n\n")
ArchivoLibro.write("Su forma base MAREEP a nivel 15 evoluciona a FLAAFFY a nivel 30 evoluciona a AMPHAROS")
ArchivoLibro.close()


with open ("Pokemones/Fuego/Tipo Fuefo.txt", "r") as archivo:
    for linea in archivo:
        
        print(linea, end="")






#crearBaseDatos()