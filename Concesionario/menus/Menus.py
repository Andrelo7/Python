from asyncio.windows_events import NULL
from agregar.Agregausuario import _usuariosRegistrados
from clas.Usuario import Usuario
user = Usuario('', '',
               '', '', '')


def buscarUsuario(correo):
    for usuario in _usuariosRegistrados:
        if usuario.correo == correo:
            user.nombre = usuario.nombre
            user.apellido = usuario.apellido
            user.correo = usuario.correo
            user.password = usuario.password
            user.nivelUsu = usuario.nivelUsu
            return True


def validarContrasenia(password):
    if user.password == str(password):
        print('BIENVENIDO')
        return [True, user.nivelUsu]


def menu(args):
    if(args == 1):
        return menuAdmin()
    elif args == 2:
        return menuEmpleado()
    else:
        return menuInvitado()


def menuAdmin():
    return "Menu Admin"


def menuEmpleado():
    return "Menu Empleado"


def menuInvitado():
    return "Menu Invitado" 