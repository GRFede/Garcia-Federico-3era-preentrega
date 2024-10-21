from django import forms

class CrearPersonalFormulario(forms.Form):
    nombres = forms.CharField(max_length=20)
    apellidos = forms.CharField(max_length=20)
    edad = forms.IntegerField()