from django import forms

class PersonalFormularioBase(forms.Form):
    nombres = forms.CharField(max_length=20)
    apellidos = forms.CharField(max_length=20)
    edad = forms.IntegerField()

class CrearPersonalFormulario(PersonalFormularioBase):...

class EditarPersonalFormulario(PersonalFormularioBase):...

class BuscarPersonalFormulario(forms.Form):
    apellidos = forms.CharField(max_length=20, required=False)

