from django import forms
from .models import Inmuebles, Empleados, CarritosCompra


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class InmuebleCreate(forms.ModelForm):
    class Meta:
        model = Inmuebles
        fields = '__all__'


class DomiciliariosCreate(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = '__all__'


class CarritoCreate(forms.ModelForm):
    class Meta:
        model = CarritosCompra
        fields = '__all__'