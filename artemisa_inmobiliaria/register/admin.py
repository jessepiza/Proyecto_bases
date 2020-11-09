from django.contrib import admin
from .models import Empleados, Clientes, Categorias, CargosEmpleado


@admin.register(Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
   list_display = ('nombre', 'apellido', 'cedula_empleado', 'nom_cargo')

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
   list_display = ('cedula_ciudadania', 'nombre', 'apellido', 'direccion', 'ciudad', 'numero_telefono')

@admin.register(CargosEmpleado)
class CargosEmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nom_cargo', 'salario', 'horas_semanales')
