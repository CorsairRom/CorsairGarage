from django.urls import path, include
from page.views import index, perfil

urlpatterns = [
    path('', index, name= "index"),
    path('/Perfil', perfil, name= "perfil")
]
