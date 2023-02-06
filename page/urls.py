from django.urls import path, include
from page.views import index, perfil, get_client,get_moto,create_client, add_Mbike, dashboard, consulta_cliente

urlpatterns = [
    path('', index, name= "index"),
    path('perfil/', perfil, name= "perfil"),
    path('dashboard/', dashboard, name= "dashboard"),
    path('create-cliente/', consulta_cliente, name= "create-cliente"),
    path('get_client/<str:rut>', get_client, name= "get_client"),
    path('get_moto/<str:patente>', get_moto, name= "get_moto"),
    path('create-client/', create_client, name= "create-client"),
    path('add-Mbike/<str:rut>', add_Mbike, name= "add-Mbike"),
]
