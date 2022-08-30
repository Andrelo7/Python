import sqlite3 

def crearBaseDatos():
    con = sqlite3.connect('cursoPython.db')
    con.commit()
    con.close()

def crearTabla():
    con = sqlite3.connect('cursoPython.db')
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE alumnos(name text, edad integer, localidad text)""")
    con.commit()
    con.close()

def InsertarDatos (nombre, edad, localidad):
    con = sqlite3.connect("cursoPython.db")
    cursor = con.cursor()
    sentencia = f'INSERT INTO alumnos VALUES("{nombre}",{edad},"{localidad}")'
    cursor.execute(sentencia)
    con.commit
    con.close

def LeerDato():
    con = sqlite3.connect("cursoPython.db")
    cursor = con.cursor()
    sentencia = f'SELECT * FROM alumnos'
    cursor.execute(sentencia)
    datos = cursor.fetchall()
    con.commit()
    con.close()
    print(datos)

def buscar(nombre):
    con = sqlite3.connect("cursoPython.db")
    cursor = con.curso()
    instruccion = f'SELECT * FROM alumnos where name="{nombre}"'
    cursor.execute(instruccion)
    valores = cursor.fetchall()
    con.commit()
    con.close()
    print(valores)

def actualizar(nombre):
    con = sqlite3.connect("cursoPython.db")
    cursor = con.curso()
    instruccion = f'UPDATE alumnos SET edad = 30 where name= "{nombre}"'
    cursor.execute(instruccion)
    valores = cursor.fetchall()
    con.commit()
    con.close



#crearBaseDatos()
crearTabla()
InsertarDatos("Rimuru", 30, "Tempest")
InsertarDatos("Kaneki", 22, "Tokio")
InsertarDatos("Cincos", 33, "Kamino")

LeerDato()
