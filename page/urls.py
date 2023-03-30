from django.urls import path, include
from page.views import add_service, delete_detail, detail_service, generate_repair_order, index, list_services, log_out, sign_in, get_client,get_moto, \
                       add_Mbike, dashboard, consulta_cliente, get_moto_rut, render_pdf_view, valve_service,view_bikes_client, list_client, list_motos

urlpatterns = [
    path('', index, name= "index"),
    path('sign-in/', sign_in, name= "sign-in"),
    path('log-out/', log_out, name= "log-out"),
    path('dashboard/', dashboard, name= "dashboard"),
    path('create-cliente/<str:rut2>', consulta_cliente, name= "create-cliente"), #funcionando
    path('valve-service/', valve_service, name= "valve-service"),
    path('add-service/', add_service, name= "add-service"),
    path('list-services/', list_services, name= "list-services"),
    path('list-client/', list_client, name= "list-client"),
    path('list-motos/', list_motos, name= "list-motos"),
    path('get_client/<str:rut>', get_client, name= "get_client"),
    path('get_moto/<str:patente>', get_moto, name= "get_moto"),
    path('get_moto_rut/<str:rut>', get_moto_rut, name= "get_moto_rut"),
    # path('create-client/<str:rut2>', create_client, name= "create-client"), borrar
    path('add-Mbike/<str:rut>', add_Mbike, name= "add-Mbike"),
    path('view-bikes-client/<str:rut>', view_bikes_client, name= "view-bikes-client"),
    path('generate-repair-order/<str:rut>/<str:patente>/<int:ficha_id>', generate_repair_order, name= "generate-repair-order"),
    path('detail-service/<str:rut>/<str:patente>/<int:ficha>', detail_service, name= "detail-service"),
    path('delete-detail/<str:id>/<str:rut>/<str:patente>/<int:ficha>', delete_detail, name= "delete-detail"),
    path('render_pdf_view/<str:rut>/<str:patente>/<int:ficha_id>/<int:desc>/<int:total>/<int:totalFinal>', render_pdf_view, name= "render_pdf_view"),
]
