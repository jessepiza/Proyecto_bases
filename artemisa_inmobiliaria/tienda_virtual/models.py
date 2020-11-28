# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CargosEmpleado(models.Model):
    nom_cargo = models.CharField(db_column='Nom_cargo', primary_key=True, max_length=50)  # Field name made lowercase.
    salario = models.IntegerField(db_column='Salario')  # Field name made lowercase.
    horas_semanales = models.SmallIntegerField(db_column='Horas_semanales')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cargos_empleado'


class CarritosCompra(models.Model):
    id_carrito = models.SmallAutoField(db_column='Id_carrito', primary_key=True)  # Field name made lowercase.
    num_item = models.SmallIntegerField(db_column='Num_item')  # Field name made lowercase.
    fecha_ingreso = models.DateField(db_column='Fecha_ingreso', blank=True, null=True)  # Field name made lowercase.
    fecha_caducidad = models.DateField(db_column='Fecha_caducidad')  # Field name made lowercase.
    cedula_ciudadania = models.OneToOneField('Clientes', models.DO_NOTHING, db_column='Cedula_ciudadania', blank=True, null=True)  # Field name made lowercase.
    checkout = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Carritos_compra'


class Categorias(models.Model):
    id_categoria = models.SmallIntegerField(db_column='Id_categoria', primary_key=True)  # Field name made lowercase.
    tipo_inmueble = models.CharField(db_column='Tipo_inmueble', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categorias'


class Clientes(models.Model):
    cedula_ciudadania = models.BigIntegerField(db_column='Cedula_ciudadania', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=50)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=50)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=50)  # Field name made lowercase.
    numero_telefono = models.BigIntegerField(db_column='Numero_telefono')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clientes'


class Empleados(models.Model):
    id_empleado = models.SmallAutoField(db_column='Id_empleado', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=50)  # Field name made lowercase.
    cedula_empleado = models.BigIntegerField(db_column='Cedula_empleado')  # Field name made lowercase.
    nom_cargo = models.ForeignKey(CargosEmpleado, models.DO_NOTHING, db_column='Nom_cargo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empleados'


class Extras(models.Model):
    id_extra = models.SmallIntegerField(db_column='Id_extra', primary_key=True)  # Field name made lowercase.
    nombre_extra = models.CharField(db_column='Nombre_extra', max_length=45)  # Field name made lowercase.
    cantidad = models.SmallIntegerField(db_column='Cantidad')  # Field name made lowercase.
    id_inmueble = models.ForeignKey('Inmuebles', models.DO_NOTHING, db_column='Id_inmueble')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Extras'
        unique_together = (('id_extra', 'id_inmueble'),)


class Inmuebles(models.Model):
    id_inmueble = models.SmallIntegerField(db_column='Id_inmueble', primary_key=True)  # Field name made lowercase.
    direccion_inmueble = models.CharField(db_column='Direccion_inmueble', max_length=50)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=50)  # Field name made lowercase.
    area = models.DecimalField(db_column='Area', max_digits=8, decimal_places=3)  # Field name made lowercase.
    numero_habitaciones = models.SmallIntegerField(db_column='Numero_habitaciones', blank=True, null=True)  # Field name made lowercase.
    numero_baños = models.SmallIntegerField(db_column='Numero_baños', blank=True, null=True)  # Field name made lowercase.
    estrato = models.SmallIntegerField(db_column='Estrato')  # Field name made lowercase.
    precio = models.BigIntegerField(db_column='Precio')  # Field name made lowercase.
    antiguedad = models.IntegerField(db_column='Antiguedad')  # Field name made lowercase.
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='Id_categoria', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inmuebles'


class Ventas(models.Model):
    num_venta = models.SmallAutoField(db_column='Num_venta', primary_key=True)  # Field name made lowercase.
    pago_inicial = models.BigIntegerField(db_column='Pago_inicial')  # Field name made lowercase.
    pago_final = models.BigIntegerField(db_column='Pago_final')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    id_carrito = models.OneToOneField(CarritosCompra, models.DO_NOTHING, db_column='Id_carrito', blank=True, null=True)  # Field name made lowercase.
    id_empleado = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='Id_empleado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ventas'


class ManyInmuebleHasManyCarritoCompra(models.Model):
    id_inmueble_inmueble = models.OneToOneField(Inmuebles, models.DO_NOTHING, db_column='Id_inmueble_Inmueble', primary_key=True)  # Field name made lowercase.
    id_carrito_carrito_compra = models.ForeignKey(CarritosCompra, models.DO_NOTHING, db_column='Id_carrito_Carrito_compra')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'many_Inmueble_has_many_Carrito_compra'
        unique_together = (('id_inmueble_inmueble', 'id_carrito_carrito_compra'),)
