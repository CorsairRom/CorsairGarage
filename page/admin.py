from django.contrib import admin
from .models import HoraHombre, Cliente, Vehiculo, Servicio, Detalle, Ficha_ingreso,Insumos, Orden_trabajo, Trabajador, Falla

admin.site.register(HoraHombre)
admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Detalle)
admin.site.register(Vehiculo)
admin.site.register(Ficha_ingreso)
admin.site.register(Insumos)
admin.site.register(Orden_trabajo)
admin.site.register(Trabajador)
admin.site.register(Falla)
