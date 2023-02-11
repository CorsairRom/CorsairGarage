from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Cliente, HoraHombre, Vehiculo, Servicio
from .forms import ClienteForm, ServicioForm, VehiculoForm, buscarRut


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

def get_moto_rut(request, rut):
    moto = list(Vehiculo.objects.filter(rut_cli = rut).values())
    if (len(moto)>0):
        data = {'message': "success", 'moto': moto}
    else:
        data = {'message': "error"}
    
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

def view_bikes_client(request, rut):
    Mbikes = Vehiculo.objects.filter(rut_cli = rut)
    client = Cliente.objects.get(rut_cli = rut)
    
    print(Mbikes.count())
    print(client)
    data = {
        "Mbikes" : Mbikes,
        "client" : client, 
    }
    return render(request, "app/view-bikes-client.html", data)


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

def list_services(request):
    services = Servicio.objects.all()
    data = {
        "services": services
    }
    return render(request, "app/list-services.html", data)

def add_service(request):
    form = ServicioForm(request.POST or None)
    data = {
        "form": form,
    }
    hh = HoraHombre.objects.all()
    service_data = Servicio.objects.latest('id')
    last_id = str(service_data.id).split("-")[1]
    new_id = int(last_id)+1
    print(new_id)
    if request.method == "POST":
        form2 = ServicioForm(data= request.POST)
        if form2.is_valid():
            form2.save(commit=False)
            datos = form2.cleaned_data
            key = str(datos.get("id_hh")).split(" ")[0]
            if key == "Básico":
                code = "CXB-"+str(new_id) 
            elif key == "Eléctrico":
                code = "CXE-"+str(new_id)
            else:
                code = "CXT-"+str(new_id)
            print(code)
            service = Servicio()
            service.nombre_sv = datos.get("nombre_sv")
            service.desc_sv = datos.get("desc_sv")
            service.hrs_240 = datos.get("hrs_240")
            service.hrs_500 = datos.get("hrs_500")
            service.hrs_800 = datos.get("hrs_800")
            service.hrs_810 = datos.get("hrs_810")
            service.tipo_sv = datos.get("tipo_sv")
            service.id_hh = datos.get("id_hh")
            service.id = str(code)
            service.save()
            return redirect(list_services)
        else:
            data["form"] = form2
    
    return render(request, "app/add-service.html", data)