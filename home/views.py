from ast import Return
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random
from django.shortcuts import render, redirect
from home.models import Persona
from home.forms import PersonaFormulario, BusquedaFormulario


def hola(request):
    return HttpResponse("<h1>Buenos dias</h1>")


def fecha(request):
    fecha_actual= datetime.now()
    return HttpResponse(f" la fecha y hora es {fecha_actual}")


def calcular_fecha(request, edad):
    fecha= datetime.now().year - edad
    return HttpResponse(f" Tu fecha de nac es: {edad} para la fecha {fecha}")

def mi_template(request):
    cargar_archivo = open(r"D:\Desktop\clases-python\proyecto-clases\home\templates\mi_template.html", "r")

    template= Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto= Context()

    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
    template = loader.get_template("home/tu_template.html")
    template_renderizado= template.render({"persona": nombre})

    return HttpResponse(template_renderizado)

def prueba_template(request):
    mi_contexto= {"rango":list(range(1,11)),
                  "valor_aleatorio": random.randrange(1,11)
                }

    template = loader.get_template("home/prueba_template.html")
    template_renderizado= template.render(mi_contexto)

    return HttpResponse(template_renderizado)

def crear_persona(request):
    
    if request.method == 'POST':
        
        formulario = PersonaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_nacimiento= data.get('fecha_nacimiento', datetime.now())
            persona = Persona(nombre=nombre, apellido=apellido, edad=edad,fecha_nacimiento=fecha_nacimiento)
            persona.save()
            
            return redirect("ver_personas")
        
    formulario= PersonaFormulario()
    return render(request, 'home/crear_persona.html', {'formulario': formulario})
    


def ver_personas(request):
    nombre=request.GET.get('nombre', None)
    
    if nombre:
        personas= Persona.objects.filter(nombre__icontains=nombre)
    else:
        personas= Persona.objects.all()
        
    formulario = BusquedaFormulario()
    
    return render(request, "home/ver_persona.html", {"personas": personas, "formulario": formulario})
    # template = loader.get_template("ver_persona.html")
    # template_renderizado= template.render({"personas": personas})
    # return HttpResponse(template_renderizado)

def index(request):
    
    return render(request, "home/index.html")
   