from django.shortcuts import render
from inicio.models import Persona

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contact.html')

def resume(request):
    return render(request, 'resume.html')

def proyectos(request):
    return render(request, 'projects.html')


def principal(request):
    return render(request, "principal.html")

def crear_persona(request):
    
    persona=Persona (nombre='federico', apellido='garcia', fecha_nacimiento=1991/6/8)
    persona.save()

    return render(request, 'persona.html')

def buscar_persona(request):

    return render(request, 'buscar_persona.html', {'persona' : ''})