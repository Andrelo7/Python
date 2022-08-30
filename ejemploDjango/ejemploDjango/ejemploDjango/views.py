from cgitb import html
from datetime import datetime
from turtle import title
from django.template import Template, Context
from django.http import HttpResponse

from ejemploDjango.Funciones import ns200

#cincos
#leg501


def holaMundo(request):
    return HttpResponse("Hola, hay asado?")

def chauMundo(request):
    return HttpResponse("Chau chau")


def prueba(request):

    sumate="Holaaa"

    ruta = "Plantilla\prueba.html"
    archivo_externo = open(ruta)
    plt = Template(archivo_externo.read())
    archivo_externo.close()
    ctx = Context({"bambam":sumate})
    plt_render=plt.render(ctx)
    return HttpResponse(plt_render)


def Foro(request):
    nombre = "InfoMotos"
   
    ruta =  "Plantilla\ForoMotos.html"
    archivo_externo = open(ruta)
    plt = Template(archivo_externo.read())
    archivo_externo.close()
    ctx = Context({"nommbreweb": nombre})
    plt_render=plt.render(ctx)
    return HttpResponse (plt_render)

def Duke(request):
    nombre = "Duke"
   
    ruta =  "Plantilla\duke200.html"
    archivo_externo = open(ruta)
    plt = Template(archivo_externo.read())
    archivo_externo.close()
    ctx = Context({"nommbreweb": nombre})
    plt_render=plt.render(ctx)
    return HttpResponse (plt_render)

def Rouser(request):
    nombre = "Rouser"
   
    ruta =  "Plantilla\moto200.html"
    archivo_externo = open(ruta)
    plt = Template(archivo_externo.read())
    archivo_externo.close()
    ctx = Context({"nommbreweb": nombre})
    plt_render=plt.render(ctx)
    return HttpResponse (plt_render)

def Tornado(request):
    nombre = "Tornado"
   
    ruta =  "Plantilla\Tornadoxr250.html"
    archivo_externo = open(ruta)
    plt = Template(archivo_externo.read())
    archivo_externo.close()
    ctx = Context({"nommbreweb": nombre})
    plt_render=plt.render(ctx)
    return HttpResponse (plt_render)

def Skua150(request):
    nombre = "Skua150"
   
    ruta =  "Plantilla\skua150.html"
    archivo_externo = open(ruta)
    plt = Template(archivo_externo.read())
    archivo_externo.close()
    ctx = Context({"nommbreweb": nombre})
    plt_render=plt.render(ctx)
    return HttpResponse (plt_render)


def Donaciones(request):
    nombre = "Donaciones"
   
    ruta =  "Plantilla\donaciones.html"
    archivo_externo = open(ruta)
    plt = Template(archivo_externo.read())
    archivo_externo.close()
    ctx = Context({"nommbreweb": nombre})
    plt_render=plt.render(ctx)
    return HttpResponse (plt_render)

