from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Cliente, Vehiculo
from .forms import ClienteForm, VehiculoForm


# ----------------PAGE SECTION!--------------------------------

def index(request):

    return render(request, "page/index.html")




# ----------------APP SECTION!--------------------------------

def dashboard(request):
    
    return render(request, "app/dashboard.html")

def consulta_cliente(request):
    form = ClienteForm (request.POST or None)
    data = {
        "form" : form   
    } 
    if request.method == "POST":
        form2 = ClienteForm(data = request.POST)
        if form2.is_valid():
            form2.save(commit=False)
            datos = form2.cleaned_data
            client = Cliente()
            client.rut_cli = datos.get("rut_cli")
            client.nombre_cli = datos.get("nombre_cli")
            client.apellido_cli = datos.get("apellido_cli")
            client.direccion_clie = datos.get("direccion_clie")
            client.celular_cli = datos.get("celular_cli")
            client.save()
            return redirect('add-Mbike', datos.get("rut_cli"))
            
    else:
        form = ClienteForm()
    return render(request, "app/create-cliente.html", data)

def perfil(request):
    
    
    return render(request, "page/perfil.html")

def get_client(_request, rut):
    # client = list(Cliente.objects.values())
    client = list(Cliente.objects.filter(rut_cli=rut).values())
    if (len(client)>0):
        data = {'message': "success", 'cliente': client}
    else:
        data = {'message': "error"}
    return JsonResponse(data)

def get_moto(request, patente):
    moto = list(Vehiculo.objects.filter(patente_vh=patente).values())
    print(moto)
    if (len(moto)>0):
        data = {'message': "success", 'Mbike': moto}
    else:
        data = {'message': "error"}
        # return redirect( to = "create_client" )
    return JsonResponse(data)

def create_client(request):
    form = ClienteForm (request.POST or None)
    data = {
        "form" : form
    }
    if request.method == "POST":
        form2 = ClienteForm(request.POST)
        if form2.is_valid():
            form2.save()
            datos = form2.cleaned_data
            client = Cliente()
            client.rut_cli = datos.get("rut_cli")
            client.nombre_cli = datos.get("nombre_cli")
            client.apellido_cli = datos.get("apellido_cli")
            client.direccion_clie = datos.get("direccion_clie")
            client.celular_cli = datos.get("celular_cli")
            client.save()
        else:
            return render(request, "page/create-client.html", {"form": form2})   
    return render(request, "app/create-client.html", data)

def add_Mbike(request, rut):
    form = VehiculoForm(request.POST or None, initial={'rut_cli': rut})
    data = {
        "form" : form
    }
    if request.method == "POST":
        form2 = VehiculoForm(data = request.POST)
        if form.is_valid():
            form.save()
            datos = form.cleaned_data
            Mbike = Vehiculo()
            Mbike.patente_vh = datos.get("patente_vh")
            Mbike.marca_vh = datos.get("marca_vh")
            Mbike.modelo_vh = datos.get("modelo_vh")
            Mbike.cilindrada_vh = datos.get("cilindrada_vh")
            Mbike.kilometraje_vh = datos.get("kilometraje_vh")
            Mbike.rut_cli = datos.get("rut_cli")
            Mbike.save()
            return redirect(dashboard)
        else:
            data["form"] = form2
    return render(request, "app/add-Mbike.html", data)