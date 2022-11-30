"""cabain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cabin_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listado_regiones/', views.listado_regiones, name='listado_regiones'),
    path('ingresar_region/', views.ingresar_region, name='ingresar_region'),
    path('listado_ciudades/', views.listado_ciudades, name='listado_ciudades'),
    path('ingresar_ciudades/', views.ingresar_ciudades, name='ingresar_ciudad'),
    path('iniciar_sesion/',views.iniciar_sesion, name='iniciar_sesion'),
    path('registrarse/', views.resgistrar_usuario, name='registro'),
    path('proyecto_nuevo/', views.crear_proyecto, name='crear_proyecto'),
    path('', views.main_menu, name='menu_principal'),
    path('payment_method/', views.payment_method , name='payment_method'),
    path('worken/', views.ingresar_maestro, name='ingresar_maestro'),
    path('listado_maestro/', views.listado_maestro, name='listado_maestro')
]
