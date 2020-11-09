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

    def __str__(self):
        return self.nom_cargo

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
    nombre_extra = models.SmallIntegerField(db_column='Nombre_extra')  # Field name made lowercase.
    cantidad = models.SmallIntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    id_inmueble = models.ForeignKey('Inmuebles', models.DO_NOTHING, db_column='Id_inmueble')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Extras'


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
    id_empleado = models.SmallIntegerField(db_column='Id_empleado', blank=True, null=True)  # Field name made lowercase.
    id_carrito = models.OneToOneField(CarritosCompra, models.DO_NOTHING, db_column='Id_carrito', blank=True, null=True)  # Field name made lowercase.
    id_empleado1 = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='Id_empleado1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ventas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ManyInmuebleHasManyCarritoCompra(models.Model):
    id_inmueble_inmueble = models.OneToOneField(Inmuebles, models.DO_NOTHING, db_column='Id_inmueble_Inmueble', primary_key=True)  # Field name made lowercase.
    id_carrito_carrito_compra = models.ForeignKey(CarritosCompra, models.DO_NOTHING, db_column='Id_carrito_Carrito_compra')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'many_Inmueble_has_many_Carrito_compra'
        unique_together = (('id_inmueble_inmueble', 'id_carrito_carrito_compra'),)
