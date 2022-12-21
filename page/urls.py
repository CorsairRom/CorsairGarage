from django.urls import path, include

from page.views import index

urlpatterns = [
    path('', index, name= "index")
]
