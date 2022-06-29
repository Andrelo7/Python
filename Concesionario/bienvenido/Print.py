from info.Info import crearUsuarios, crearAuto


def bienvenida():
    print('BIENVENIDO A LA CONCESIONARIA BAMBAM!!!')
    print("    //   ) )     // | |     /|    //| |     //   ) )     // | |     /|    //| |")
    print("   //___/ /     //__| |    //|   // | |    //___/ /     //__| |    //|   // | |")
    print("  / __  (      / ___  |   // |  //  | |   / __  (      / ___  |   // |  //  | |")
    print(" //    ) )    //    | |  //  | //   | |  //    ) )    //    | |  //  | //   | |")
    print("//____/ /    //     | | //   |//    | | //____/ /    //     | | //   |//    | |")
    crearUsuarios()
    crearAuto()


def msjUsuario():
    return input('Ingrese Correo Electronico: ')


def msjErrorUsuario():
    print('Usuario Incorrecto')


def msjPassword():
    return input('Ingrese Password: ')


def msjErrorPassword():
    print('Password Incorrecta')