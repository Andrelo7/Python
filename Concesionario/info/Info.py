from clas.Usuario import Usuario
from clas.Auto import Auto
from agregar.Agregausuario import agregaUsuarios, printUsuarios
from agregar.Agregarauto import agregaAutos


def crearUsuarios():
    usuario = Usuario('Juanchope', 'Messi',
                      'juanchope_messi@gmail.com', 'ManCity10', 1)
    agregaUsuarios(usuario)
    usuario = Usuario('Kun', 'Aguero',
                      'kuniaguero.10@gmail.com', 'vamoajuga', 2)
    agregaUsuarios(usuario)
    usuario = Usuario('Anakin', 'Skywalker',
                      'skywalker@gamil.com', 'r2d2', 3)
    agregaUsuarios(usuario)
    usuario = Usuario('Alexis', 'Lorda',
                      'alexis_lorda@gmail.com', 'fifa', 1 )
    agregaUsuarios(usuario)
    usuario = Usuario('Cristian', 'Rodriguez',
                      'cris_rodriguez@gmail.com', 'pagateelasadocris', 2 )
    agregaUsuarios(usuario)

def crearAuto():
    auto = Auto('Toyota', 'Hilux', 0, 'Perfecto para trabajar')
    agregaAutos(auto)
    auto = Auto('Nissan', 'GTR-R34', 35000, 'Una leyenda viviente')
    agregaAutos(auto)
    auto = Auto('Ford', 'Mustang', 1000, 'Una joya americana')
    agregaAutos(auto)


def insertarAuto():
    marca = input('Ingrese la marca: ')
    modelo = input('Ingrese la modelo:')
    km = input('Ingrese el kilometraje: ')
    detalle = input('Ingrese los detalles')
    auto_ingresado = Auto(marca, modelo,  km, detalle)
    agregaAutos(auto_ingresado)