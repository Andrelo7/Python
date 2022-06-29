from info.Info import insertarAuto
from bienvenido.Print import *
from menus.Menus import buscarUsuario, validarContrasenia, menu
from info.Info import insertarAuto

bienvenida()
userOk = buscarUsuario(msjUsuario())
intentos = 3
try:
    if(userOk):

        usuarioconPass = validarContrasenia(msjPassword())
        while userOk:
            if(usuarioconPass[0]):
                userOk = menu(usuarioconPass[1])
    else:
        print('No se encontro el Usuario')

finally:
    print('Gracias por Visitarnos')