from django.http import HttpResponse

def ns200 (request):
    texto="""
        <html>
        </body>
        <h1>
        BAJAJ ROUSER NS200
        <h1>
        </body>
        <html>
        \n
        <html>
        </body>
        <h3>
        Rouser ("Pulsar" en otros paises) NS200 Utilizanda el primer motor de triple bujía y 4 válvulas con DTS-i del mundo, la moto está diseñada para sorprendernos con su tecnología y su apariencia agresiva.
        Alguna de sus caracteristicas son:

        CILINDRADA:         195.5 cc
        POTENCIA:           23.52
        TORQUE:             18.3 @ 8000 (Nm @ RPM)
        MOTOR:              SOHC 4V, refrigerado por líquido
        TANQUE DE NAFTA:    (Reserva/Utilizable) 12 Litros
        DISCOS DE FRENO:    con Cáliper Flotante
        CAJA DE CAMBIOS:    6 Marchas

        LINK PARA DESCARGAR EL MANUAL
        https://www.globalbajaj.com/media/20668/manual-bajaj-pulsar-ns200-y-as200-png.pdf
        <h3>
        </body>
        <html>
        
    """
    return HttpResponse(texto)


def duke200 (request):
    texto="""
        <html>
        </body>
        <h1>
        KTM DUKE 200
        <h1>
        </body>
        <html>
        \n
        <html>
        </body>
        <h3>
    
        MOTOR:  	        Monocilíndrico, 4 tiempos, 4 válvulas, DOHC, refrigerado por líquido
        CILINDRADA:	        199,5 cc
        POTENCIA:	        26 cv 
        ALIMENTACION:	    Inyección electrónica
        ENCENDIDO:	        TCI
        DISCOS DE FRENO:    con Cáliper Flotante
        ARRANQUE:	        Eléctrico
        TRANSMISION:	    6 velocidades
        TANQUE DE NAFTA:    11 Litros
        <h3>
        </body>
        <html>

    """
    return HttpResponse(texto)

def xr250 (request):
    texto="""
        <html>
        </body>
        <h1>
        HONDA XR 250 (TORNADO)
        <h1>
        </body>
        <html>
        \n
        <html>
        </body>
        <h3>
    
        MOTOR:  	        Monocilindro, DOHC, 4 tiempos, refrigerado por aire
        CILINDRADA:	        249 cc
        ENCENDIDO:          CDI (ignición por descarga capacidad)
        ARRANQUE:	        Eléctrico
        TRANSMISION:        6 velocidades
        TANQUE DE NAFTA:    Reserva/Utilizable) 15 Litros
        FRENOS:             Delantera disco / Trasera tambor

        <h3>
        </body>
        <html>
        
    """
    return HttpResponse(texto)