from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render, redirect
from .models import Inmuebles, Extras, Empleados, Ventas
from django.contrib.auth import authenticate, login
from .forms import LoginForm, InmuebleCreate, DomiciliariosCreate, CarritoCreate
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


def upload_inmueble(request):
    upload = InmuebleCreate()
    if request.method == 'POST':
        upload = InmuebleCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse('Los datos a cargar son inválidos.')
    else:
        return render(request, 'tienda_virtual/upload_form_inmueble.html', {'upload_form': upload})

def perfil(request):
    return render(request, 'tienda_virtual/Perfil_admin_sara.html')

def editar_inmueble(request):
    shelf = Inmuebles.objects.all()
    return render(request, 'tienda_virtual/editar_inmueble.html', {'shelf' : shelf})

def editar_domiciliario(request):
    shelf = Empleados.objects.filter(nom_cargo='Domiciliario')
    return render(request, 'tienda_virtual/editar_domiciliario.html', {'shelf' : shelf})

def update_inmueble(request, id_inmueble):
    id_inmueble = int(id_inmueble)
    try:
        inmueble_sel = Inmuebles.objects.get(id_inmueble=id_inmueble)
    except Inmuebles.DoesNotExist:
        return redirect('index')
    inmueble_form = InmuebleCreate(request.POST or None, instance=inmueble_sel)
    if inmueble_form.is_valid():
        inmueble_form.save()
        return redirect('index')
    return render(request, 'tienda_virtual/upload_form_inmueble.html', {'upload_form': inmueble_form})


def delete_inmueble(request, id_inmueble):
    id_inmueble = int(id_inmueble)
    try:
        inmueble_sel = Inmuebles.objects.get(id_inmueble=id_inmueble)
        extras_sel = Extras.objects.filter(id_inmueble=id_inmueble)
    except Inmuebles.DoesNotExist:
        return redirect('index')
    for i in range(len(extras_sel)):
        extras_sel[i].delete()
    inmueble_sel.delete()
    return redirect('index')

def upload_domiciliarios(request):
    upload = DomiciliariosCreate()
    if request.method == 'POST':
        upload = DomiciliariosCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse('Los datos a cargar son inválidos.')
    else:
        return render(request, 'tienda_virtual/upload_form_domiciliario.html',{'upload_dom_form': upload})


def update_domiciliarios(request, id_empleado):
    id_empleado = int(id_empleado)
    try:
        dom_sel = Empleados.objects.get(id_empleado=id_empleado)
    except Empleados.DoesNotExist:
        return redirect('index')
    dom_form = DomiciliariosCreate(request.POST or None, instance=dom_sel)
    if dom_form.is_valid():
        dom_form.save()
        return redirect('index')
    return render(request,'tienda_virtual/upload_form_domiciliario.html',{'upload_dom_form': dom_form})


def delete_domiciliarios(request, id_empleado):
    dom_id = int(id_empleado)
    try:
        dom_sel = Empleados.objects.get(id_empleado=dom_id)
    except Empleados.DoesNotExist:
        return redirect('index')
    dom_sel.delete()
    return redirect('index')


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
                draw.text((150, 100), 'Id Inmueble: ' + '\n''Dirección: ' + '\n' +'Estrato: ' + '\n' + 'Sector: ' '\n' +'Precio: '+ '\n' +'Area: '
                                     + '\n' + 'Antigüedad: ' + '\n' + 'No. Habitaciones: ' '\n' + 'No. Baños: ', purple, font=font)
                draw.text((450, 100), str(q.id_inmueble) + '\n' + q.direccion_inmueble + '\n' + str(q.estrato) + '\n' + q.sector + '\n' + '$' + str(q.precio)
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
                draw.text((150, 100),
                          'Id Inmueble: ' + '\n''Dirección: ' + '\n' + 'Estrato: ' + '\n' + 'Sector: ' '\n' + 'Precio: ' + '\n' + 'Area: '
                          + '\n' + 'Antigüedad: ' + '\n' + 'No. Habitaciones: ' '\n' + 'No. Baños: ', purple, font=font)
                draw.text((450, 100), str(q.id_inmueble) + '\n' + q.direccion_inmueble + '\n' + str(
                    q.estrato) + '\n' + q.sector + '\n' + '$' + str(q.precio)
                          + '\n' + str(round(q.area, 2)) + ' m²' + '\n' + str(q.antiguedad) + ' años' + '\n' + str(
                    q.numero_habitaciones)
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
                draw.text((150, 100),
                          'Id Inmueble: ' + '\n''Dirección: ' + '\n' + 'Estrato: ' + '\n' + 'Sector: ' '\n' + 'Precio: ' + '\n' + 'Area: '
                          + '\n' + 'Antigüedad: ' + '\n' + 'No. Habitaciones: ' '\n' + 'No. Baños: ', purple, font=font)
                draw.text((450, 100), str(q.id_inmueble) + '\n' + q.direccion_inmueble + '\n' + str(
                    q.estrato) + '\n' + q.sector + '\n' + '$' + str(q.precio)
                          + '\n' + str(round(q.area, 2)) + ' m²' + '\n' + str(q.antiguedad) + ' años' + '\n' + str(
                    q.numero_habitaciones)
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
                draw.text((150, 100),
                          'Id Inmueble: ' + '\n''Dirección: ' + '\n' + 'Estrato: ' + '\n' + 'Sector: ' '\n' + 'Precio: ' + '\n' + 'Area: '
                          + '\n' + 'Antigüedad: ' + '\n' + 'No. Habitaciones: ' '\n' + 'No. Baños: ', purple, font=font)
                draw.text((450, 100), str(q.id_inmueble) + '\n' + q.direccion_inmueble + '\n' + str(
                    q.estrato) + '\n' + q.sector + '\n' + '$' + str(q.precio)
                          + '\n' + str(round(q.area, 2)) + ' m²' + '\n' + str(q.antiguedad) + ' años' + '\n' + str(
                    q.numero_habitaciones)
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
                draw.text((150, 100),
                          'Id Inmueble: ' + '\n''Dirección: ' + '\n' + 'Estrato: ' + '\n' + 'Sector: ' '\n' + 'Precio: ' + '\n' + 'Area: '
                          + '\n' + 'Antigüedad: ' + '\n' + 'No. Habitaciones: ' '\n' + 'No. Baños: ', purple, font=font)
                draw.text((450, 100), str(q.id_inmueble) + '\n' + q.direccion_inmueble + '\n' + str(
                    q.estrato) + '\n' + q.sector + '\n' + '$' + str(q.precio)
                          + '\n' + str(round(q.area, 2)) + ' m²' + '\n' + str(q.antiguedad) + ' años' + '\n' + str(
                    q.numero_habitaciones)
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
                draw.text((150, 100),
                          'Id Inmueble: ' + '\n''Dirección: ' + '\n' + 'Estrato: ' + '\n' + 'Sector: ' '\n' + 'Precio: ' + '\n' + 'Area: '
                          + '\n' + 'Antigüedad: ' + '\n' + 'No. Habitaciones: ' '\n' + 'No. Baños: ', purple, font=font)
                draw.text((450, 100), str(q.id_inmueble) + '\n' + q.direccion_inmueble + '\n' + str(
                    q.estrato) + '\n' + q.sector + '\n' + '$' + str(q.precio)
                          + '\n' + str(round(q.area, 2)) + ' m²' + '\n' + str(q.antiguedad) + ' años' + '\n' + str(
                    q.numero_habitaciones)
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
    upload = CarritoCreate()
    if request.method == 'POST':
        upload = CarritoCreate(request.POST, request.FILES)
        if upload.is_valid():
            return redirect('gracias')
        else:
            return HttpResponse('Los datos a cargar son inválidos.')
    else:
        return render(request, 'tienda_virtual/carrito-de-compras.html',{'upload_form': upload})

def ventas(request):
    shelf = Ventas.objects.all()
    return render(request, 'tienda_virtual/ventas.html', {'shelf':shelf})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('perfil')
                else:
                    return redirect('perfil')
            else:
                return redirect('perfil')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def gracias(request):
    return render(request, 'tienda_virtual/gracias.html')   

def signup(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            raw_password = form1.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form1 = UserCreationForm()
    return render(request, 'account/login.html', {'form': form1})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})