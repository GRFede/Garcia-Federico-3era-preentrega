from django.urls import path
from inicio.views import inicio, principal,crear_persona,resume,contacto,proyectos,buscar_persona


urlpatterns = [
    path('', inicio, name='inicio'),
    path('principal/', principal, name='principal'),
    path('persona/', crear_persona, name='crear_persona'),
    path('resume/', resume, name='resume'),
    path('contact/', contacto, name='contacto'),
    path('projects/', proyectos, name='proyectos'),
    path('buscar-persona/', buscar_persona, name='buscar_persona'),


]