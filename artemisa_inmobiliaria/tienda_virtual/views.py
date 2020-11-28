from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Inmuebles
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'tienda_virtual/base.html',)


def inmuebles(request):
    shelf = Inmuebles.objects.all()
    return render(request, 'tienda_virtual/inmuebles.html', {'shelf': shelf})


def presentacion(request):
    return render(request, 'tienda_virtual/presentacion.html',)


def contacto(request):
    return render(request, 'tienda_virtual/contacto.html',)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Usuario autenticado satisfactoriamente')
                else:
                    return HttpResponse('La cuenta está inactiva')
            else:
                return HttpResponse('Login inválido')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})