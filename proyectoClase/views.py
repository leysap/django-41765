from re import template
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template


def hola(request):
    return HttpResponse("<h1>Buenos dias</h1>")


def fecha(request):
    fecha_actual= datetime.now()
    return HttpResponse(f" la fecha y hora es {fecha_actual}")


def calcular_fecha(request, edad):
    fecha= datetime.now().year - edad
    return HttpResponse(f" Tu fecha de nac es: {edad} para la fecha {fecha}")

def mi_template(request):
    cargar_archivo = open(r"D:\Desktop\clases-python\proyecto-clases\templates\template.html", "r")

    template= Template(cargar_archivo.read())
    cargar_archivo.close()
    
    contexto= Context()

    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)