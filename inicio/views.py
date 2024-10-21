from django.shortcuts import render, redirect
from inicio.models import Personales
from inicio.forms import CrearPersonalFormulario,BuscarPersonalFormulario,EditarPersonalFormulario

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

def crear_personales(request):

    formulario = CrearPersonalFormulario()
    if request.method == 'POST':
        formulario = CrearPersonalFormulario(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            personal = Personales(nombres= data.get('nombres'), apellidos= data.get('apellidos'), edad= data.get('edad'))
            personal.save()
            return redirect('buscar_persona') 

    return render(request, 'crear_personales.html', {'form' : formulario})

def buscar_persona(request):

    formulario = BuscarPersonalFormulario(request.GET)
    if formulario.is_valid():
        apellidos=formulario.cleaned_data.get('apellidos')
        personas=Personales.objects.filter(apellidos__icontains=apellidos)
    else:
        personas= Personales.objects.all()  

    return render(request, 'buscar_persona.html', {'personas' : personas, 'form': formulario})

def ver_personas(request,id):
    persona = Personales.objects.get(id=id)
    return render(request, 'ver_personas.html', {'persona':persona})

def eliminar_persona(request,id):
    persona = Personales.objects.get(id=id)
    persona.delete()
    return redirect('buscar_persona')

def editar_persona(request, id):
    persona = Personales.objects.get(id=id)

    formulario=EditarPersonalFormulario(initial={'nombres':persona.nombres,'apellidos':persona.apellidos,'edad':persona.edad})

    if request.method == "POST":
        formulario=EditarPersonalFormulario(request.POST)
        if formulario.is_valid():
            persona.nombres=formulario.cleaned_data.get('nombres')
            persona.apellidos=formulario.cleaned_data.get('apellidos')
            persona.edad=formulario.cleaned_data.get('edad')

            persona.save()

            return redirect('buscar_persona')

    return render(request, 'editar_persona.html', {'persona': persona, 'form':formulario})
