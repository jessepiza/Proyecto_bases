from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Inmuebles, Categorias
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

# Create your views here.
def index(request):
    return render(request, 'tienda_virtual/base.html',)


def inmuebles(request):
    shelf = Inmuebles.objects.all()
    return render(request, 'tienda_virtual/inmuebles.html', {'shelf': shelf})


def presentacion(request):
    return render(request, 'tienda_virtual/presentacion.html',)


def apartaestudio(request):
    inmueble = Inmuebles.objects.filter(id_categoria=1)
    ids = Inmuebles.objects.values_list('id_inmueble').filter(id_categoria=1)
    id = [int(q[0]) for q in ids]
    lista = os.listdir("static/media/Imagenes/")
    listatot = []
    for i in id:
        img = Image.new('RGB', (800, 400), "white")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("C:/Windows/Fonts/bellb.ttf", 30)
        purple = (126, 60, 142)
        for q in inmueble:
            if i == q.id_inmueble:
                draw.text((150, 100), 'Dirección: ' + '\n' +'Estrato: ' + '\n' + 'Sector: ' '\n' +'Precio: '+ '\n' +'Area: '
                                     + '\n' + 'Antigüedad: ' + '\n' + 'No. Habitaciones: ' '\n' + 'No. Baños: ', purple, font=font)
                draw.text((450, 100), q.direccion_inmueble + '\n' + str(q.estrato) + '\n' + q.sector + '\n' + '$' + str(q.precio)
                          + '\n' + str(round(q.area, 2)) + ' m²' + '\n' + str(q.antiguedad) + ' años' + '\n' + str(q.numero_habitaciones)
                          + '\n' + str(q.numero_baños), (0, 0, 0), font=font)
        img.save('static/media/Imagenes/' + str(i) + '/z.jpg', 'JPEG')

    for i in range(len(lista)):
        if int(lista[i]) in id:
            lista2 = os.listdir("static/media/Imagenes/"+lista[i] + "/")
            aux = []
            for q in range(len(lista2)):
                aux.append('media/Imagenes/' + lista[i] + '/' + lista2[q])
            listatot.append(aux)

    apartaestudios = {'apartaestudios':inmueble,
                      'lista':listatot}
    return render(request, 'tienda_virtual/apartaestudio.html', apartaestudios)


def apartamento(request):
    inmueble = Inmuebles.objects.filter(id_categoria=2)
    ids = Inmuebles.objects.values_list('id_inmueble').filter(id_categoria=2)
    id = [int(q[0]) for q in ids]
    lista = os.listdir("static/media/Imagenes/")
    listatot = []
    for i in id:
        img = Image.new('RGB', (800, 400), "white")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("C:/Windows/Fonts/bellb.ttf", 30)
        purple = (126, 60, 142)
        for q in inmueble:
            if i == q.id_inmueble:
                draw.text((20, 100), 'Dirección: ' + '\n' +'Estrato: ' + '\n' + 'Sector: ' '\n' +'Precio: '+ '\n' +'Area: '
                                     + '\n' + 'Antigüedad: ' + '\n' + 'No. Habitaciones: ' '\n' + 'No. Baños: ', purple, font=font)
                draw.text((300, 100), q.direccion_inmueble + '\n' + str(q.estrato) + '\n' + q.sector + '\n' + '$' + str(q.precio)
                          + '\n' + str(round(q.area, 2)) + ' m²' + '\n' + str(q.antiguedad) + ' años' + '\n' + str(q.numero_habitaciones)
                          + '\n' + str(q.numero_baños), (0, 0, 0), font=font)
        img.save('static/media/Imagenes/' + str(i) + '/z.jpg', 'JPEG')
    for i in range(len(lista)):
        if int(lista[i]) in id:
            lista2 = os.listdir("static/media/Imagenes/" + lista[i] + "/")
            aux = []
            for q in range(len(lista2)):
                aux.append('media/Imagenes/' + lista[i] + '/' + lista2[q])
            listatot.append(aux)

    apartamentos = {'apartamentos': inmueble,
                      'lista': listatot}
    return render(request, 'tienda_virtual/apartamentos.html', apartamentos)


def casa(request):
    inmueble = Inmuebles.objects.filter(id_categoria=3)
    ids = Inmuebles.objects.values_list('id_inmueble').filter(id_categoria=3)
    id = [int(q[0]) for q in ids]
    lista = os.listdir("static/media/Imagenes/")
    listatot = []
    for i in id:
        img = Image.new('RGB', (800, 400), "white")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("C:/Windows/Fonts/bellb.ttf", 30)
        purple = (126, 60, 142)
        for q in inmueble:
            if i == q.id_inmueble:
                draw.text((150, 100), 'Dirección: ' + '\n' +'Estrato: ' + '\n' + 'Sector: ' '\n' +'Precio: '+ '\n' +'Area: '
                                     + '\n' + 'Antigüedad: ' + '\n' + 'No. Habitaciones: ' '\n' + 'No. Baños: ', purple, font=font)
                draw.text((450, 100), q.direccion_inmueble + '\n' + str(q.estrato) + '\n' + q.sector + '\n' + '$' + str(q.precio)
                          + '\n' + str(round(q.area, 2)) + ' m²' + '\n' + str(q.antiguedad) + ' años' + '\n' + str(q.numero_habitaciones)
                          + '\n' + str(q.numero_baños), (0, 0, 0), font=font)
        img.save('static/media/Imagenes/' + str(i) + '/z.jpg', 'JPEG')
    for i in range(len(lista)):
        if int(lista[i]) in id:
            lista2 = os.listdir("static/media/Imagenes/" + lista[i] + "/")
            aux = []
            for q in range(len(lista2)):
                aux.append('media/Imagenes/' + lista[i] + '/' + lista2[q])
            listatot.append(aux)

    casas = {'casas': inmueble,
            'lista': listatot}
    return render(request, 'tienda_virtual/casas.html',casas)


def oficina(request):
    inmueble = Inmuebles.objects.filter(id_categoria=4)
    ids = Inmuebles.objects.values_list('id_inmueble').filter(id_categoria=4)
    id = [int(q[0]) for q in ids]
    lista = os.listdir("static/media/Imagenes/")
    listatot = []
    for i in id:
        img = Image.new('RGB', (800, 400), "white")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("C:/Windows/Fonts/bellb.ttf", 30)
        purple = (126, 60, 142)
        for q in inmueble:
            if i == q.id_inmueble:
                draw.text((150, 100), 'Dirección: ' + '\n' +'Estrato: ' + '\n' + 'Sector: ' '\n' +'Precio: '+ '\n' +'Area: '
                                     + '\n' + 'Antigüedad: ' + '\n' + 'No. Habitaciones: ' '\n' + 'No. Baños: ', purple, font=font)
                draw.text((450, 100), q.direccion_inmueble + '\n' + str(q.estrato) + '\n' + q.sector + '\n' + '$' + str(q.precio)
                          + '\n' + str(round(q.area, 2)) + ' m²' + '\n' + str(q.antiguedad) + ' años' + '\n' + str(q.numero_habitaciones)
                          + '\n' + str(q.numero_baños), (0, 0, 0), font=font)
        img.save('static/media/Imagenes/' + str(i) + '/z.jpg', 'JPEG')
    for i in range(len(lista)):
        if int(lista[i]) in id:
            lista2 = os.listdir("static/media/Imagenes/" + lista[i] + "/")
            aux = []
            for q in range(len(lista2)):
                aux.append('media/Imagenes/' + lista[i] + '/' + lista2[q])
            listatot.append(aux)

    oficinas = {'oficinas': inmueble,
                'lista': listatot}
    return render(request, 'tienda_virtual/oficinas.html',oficinas)


def lote(request):
    inmueble = Inmuebles.objects.filter(id_categoria=5)
    ids = Inmuebles.objects.values_list('id_inmueble').filter(id_categoria=5)
    id = [int(q[0]) for q in ids]
    lista = os.listdir("static/media/Imagenes/")
    listatot = []
    for i in id:
        img = Image.new('RGB', (800, 400), "white")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("C:/Windows/Fonts/bellb.ttf", 30)
        purple = (126, 60, 142)
        for q in inmueble:
            if i == q.id_inmueble:
                draw.text((150, 100), 'Dirección: ' + '\n' +'Estrato: ' + '\n' + 'Sector: ' '\n' +'Precio: '+ '\n' +'Area: '
                                     + '\n' + 'Antigüedad: ' + '\n' + 'No. Habitaciones: ' '\n' + 'No. Baños: ', purple, font=font)
                draw.text((450, 100), q.direccion_inmueble + '\n' + str(q.estrato) + '\n' + q.sector + '\n' + '$' + str(q.precio)
                          + '\n' + str(round(q.area, 2)) + ' m²' + '\n' + str(q.antiguedad) + ' años' + '\n' + str(q.numero_habitaciones)
                          + '\n' + str(q.numero_baños), (0, 0, 0), font=font)
        img.save('static/media/Imagenes/' + str(i) + '/z.jpg', 'JPEG')
    for i in range(len(lista)):
        if int(lista[i]) in id:
            lista2 = os.listdir("static/media/Imagenes/" + lista[i] + "/")
            aux = []
            for q in range(len(lista2)):
                aux.append('media/Imagenes/' + lista[i] + '/' + lista2[q])
            listatot.append(aux)

    lotes = {'lotes': inmueble,
                'lista': listatot}
    return render(request, 'tienda_virtual/lotes.html',lotes)


def condominio(request):
    inmueble = Inmuebles.objects.filter(id_categoria=6)
    ids = Inmuebles.objects.values_list('id_inmueble').filter(id_categoria=6)
    id = [int(q[0]) for q in ids]
    lista = os.listdir("static/media/Imagenes/")
    listatot = []
    for i in id:
        img = Image.new('RGB', (800, 400), "white")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("C:/Windows/Fonts/bellb.ttf", 30)
        purple = (126, 60, 142)
        for q in inmueble:
            if i == q.id_inmueble:
                draw.text((150, 100), 'Dirección: ' + '\n' +'Estrato: ' + '\n' + 'Sector: ' '\n' +'Precio: '+ '\n' +'Area: '
                                     + '\n' + 'Antigüedad: ' + '\n' + 'No. Habitaciones: ' '\n' + 'No. Baños: ', purple, font=font)
                draw.text((450, 100), q.direccion_inmueble + '\n' + str(q.estrato) + '\n' + q.sector + '\n' + '$' + str(q.precio)
                          + '\n' + str(round(q.area, 2)) + ' m²' + '\n' + str(q.antiguedad) + ' años' + '\n' + str(q.numero_habitaciones)
                          + '\n' + str(q.numero_baños), (0, 0, 0), font=font)
        img.save('static/media/Imagenes/' + str(i) + '/z.jpg', 'JPEG')
    for i in range(len(lista)):
        if int(lista[i]) in id:
            lista2 = os.listdir("static/media/Imagenes/" + lista[i] + "/")
            aux = []
            for q in range(len(lista2)):
                aux.append('media/Imagenes/' + lista[i] + '/' + lista2[q])
            listatot.append(aux)

    condominios = {'condominios': inmueble,
             'lista': listatot}
    return render(request, 'tienda_virtual/condominios.html',condominios)


def domiciliarios(request):
    return render(request, 'tienda_virtual/domiciliarios.html',)


def carrito(request):
    return render(request, 'tienda_virtual/carrito-de-compras.html',)


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