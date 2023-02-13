from django.urls import path, include
from page.views import add_service, detail_service, generate_repair_order, index, list_services, perfil, get_client,get_moto,create_client, \
                       add_Mbike, dashboard, consulta_cliente, get_moto_rut,view_bikes_client

urlpatterns = [
    path('', index, name= "index"),
    path('perfil/', perfil, name= "perfil"),
    path('dashboard/', dashboard, name= "dashboard"),
    path('create-cliente/', consulta_cliente, name= "create-cliente"),
    path('add-service/', add_service, name= "add-service"),
    path('list-services/', list_services, name= "list-services"),
    path('get_client/<str:rut>', get_client, name= "get_client"),
    path('get_moto/<str:patente>', get_moto, name= "get_moto"),
    path('get_moto_rut/<str:rut>', get_moto_rut, name= "get_moto_rut"),
    path('create-client/', create_client, name= "create-client"),
    path('add-Mbike/<str:rut>', add_Mbike, name= "add-Mbike"),
    path('view-bikes-client/<str:rut>', view_bikes_client, name= "view-bikes-client"),
    path('generate-repair-order/<str:rut>/<str:patente>', generate_repair_order, name= "generate-repair-order"),
    path('detail-service/<str:rut>/<str:patente>/<int:ficha>', detail_service, name= "detail-service"),
]
