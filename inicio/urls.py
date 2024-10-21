from django.urls import path
from inicio.views import (
    inicio, 
    principal, 
    resume, 
    contacto, 
    proyectos, 
    buscar_persona, 
    crear_personales, 
    ver_personas, 
    eliminar_persona, 
    editar_persona)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('principal/', principal, name='principal'),
    path('resume/', resume, name='resume'),
    path('contact/', contacto, name='contacto'),
    path('projects/', proyectos, name='proyectos'),
    path('buscar-persona/', buscar_persona, name='buscar_persona'),
    path('crear-personales/', crear_personales, name='crear_personales'),
    path('ver-persona/<int:id>', ver_personas, name='ver_personas'),
    path('eliminar-persona/<int:id>', eliminar_persona, name='eliminar_persona'),
    path('editar-persona/<int:id>', editar_persona, name='editar_persona'),


]