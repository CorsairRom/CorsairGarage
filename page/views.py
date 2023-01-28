from django.shortcuts import render

def index(request):

    return render(request, "page/index.html")


def perfil(request):
    
    return render(request, "page/perfil.html")