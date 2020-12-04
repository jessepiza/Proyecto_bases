from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('inmueble/', views.inmuebles, name = 'inmuebles'),
    path('presentacion/', views.presentacion, name = 'presentacion'),
    path('apartamento/', views.apartamento, name = 'apartamentos'),
    path('apartaestudio/', views.apartaestudio, name = 'apartaestudio'),
    path('casa/', views.casa, name = 'casas'),
    path('oficina/', views.oficina, name = 'oficinas'),
    path('lote/', views.lote, name = 'lotes'),
    path('condominio/', views.condominio, name = 'condominios'),
    path('domiciliarios/', views.domiciliarios, name = 'domiciliarios'),
    path('carrito-de-compras/', views.carrito, name = 'carrito'),
    #path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name = 'signup'),
    path('', views.dashboard, name="dashboard"),

    path('upload_inmueble/', views.upload_inmueble, name='upload_inmueble'),
    path('upload_domiciliario/', views.upload_domiciliarios, name='upload_domiciliario'),
    path('editar_inmueble/update/<int:id_inmueble>', views.update_inmueble),
    path('editar_domiciliario/update/<int:id_empleado>', views.update_domiciliarios),
    path('editar_inmueble/delete/<int:id_inmueble>', views.delete_inmueble),
    path('editar_domiciliario/delete/<int:id_empleado>', views.delete_domiciliarios),

    path('perfil/', views.perfil, name = 'perfil'),
    path('editar_inmueble/', views.editar_inmueble, name ='editar_inmueble'),
    path('editar_domiciliario/', views.editar_domiciliario, name ='editar_domiliciario'),
    path('ventas/', views.ventas, name = 'ventas'),
    path('gracias/', views.gracias, name = 'gracias'),

    # rutas de cambio de contraseña
    # rutas de cambio de contraseña
    path('password_change/', auth_views.PasswordChangeView.as_view(), name="password_change"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
]
