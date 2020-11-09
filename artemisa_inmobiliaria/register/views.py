from .models import Clientes, Empleados, CargosEmpleado
from django.shortcuts import render


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_clientes = Clientes.objects.all().count()
    num_empleados = Empleados.objects.all().count()
    num_administrador = Empleados.objects.filter(nom_cargo='Administrador').count()

    context = {
        'num_clientes': num_clientes,
        'num_empleados': num_empleados,
        'num_administrador': num_administrador,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)