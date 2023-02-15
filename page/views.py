import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente, Detalle, Ficha_ingreso, HoraHombre, Vehiculo, Servicio
from .forms import ClienteForm, DetalleForm, Ficha_ingresoForm, OTForm, ServicioForm, VehiculoForm, buscarRut, Vehiculo_change_kmForm
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

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
            #aqui falta el return render para que no se duplique
        else:
            return render(request, "page/create-client.html", {"form": form2})   
    return render(request, "app/create-client.html", data)

def view_bikes_client(request, rut):
    Mbikes = Vehiculo.objects.filter(rut_cli = rut)
    client = Cliente.objects.get(rut_cli = rut)
    form = Ficha_ingresoForm(request.POST or None)
    fi_client = Ficha_ingreso.objects.filter(rut_cli = rut)
    # form2 = Vehiculo_change_kmForm(request.POST or None)
    data = {
        "Mbikes" : Mbikes,
        "client" : client, 
        "form" : form,
        "fi_client" : fi_client
    }
    
    if request.method == "POST":
        form2 = Ficha_ingresoForm(request.POST)
        if form2.is_valid():
            form2.save(commit=False)
            datos = form2.cleaned_data
            fi = Ficha_ingreso()
            fi.patente_vh = datos.get("patente_vh")
            patente = fi.patente_vh
            fi.rut_cli = client
            fi.observaciones_fi = datos.get("observaciones_fi")
            fi.km_mill_fi = datos.get("km_mill_fi")
            fi.mill_km_vh = datos.get("mill_km_vh")
            fi.save()
            ficha = fi.id #type: ignore
            print(ficha)
            return redirect(detail_service, rut, patente, ficha)
        else:
            data["form"] = form2 
    return render(request, "app/view-bikes-client.html", data)

def detail_service(request, rut, patente, ficha):
    form = DetalleForm(request.POST or None, initial={'id_fi': ficha})
    ficha_id = Ficha_ingreso.objects.get(id=ficha)
    detalles = Detalle.objects.filter(id_fi = ficha)
    Mbikes = Vehiculo.objects.get(patente_vh = patente)
    client = Cliente.objects.get(rut_cli = rut)
    total = 0
    totalFin = 0
    desc = 0
    for detalle in detalles:
        total += detalle.precio_servicio
    data = {
        "form": form,
        "client": client,
        "Mbikes": Mbikes,
        "detalles": detalles,
        "ficha": ficha,
        "total":total,
        "totalFin":totalFin,
        "ficha_id": ficha_id,
        "desc": desc
    }
    if totalFin ==0:
        data["totalFin"] = total
    if request.method == 'GET':
        descData = request.GET.get('descuento', None)
        if descData is not None:
            desc= int(descData)
            if total > 1:
                porcentaje = total*(desc/100)
                totalFinal = round(total-porcentaje)
                data["desc"] = descData
                data["totalFin"] = totalFinal
                       
    cc = Mbikes.cilindrada_vh
    def calculo(cc, sv):
        id_hh = sv.id_hh.precio_hh
        if cc < 240:
            horas = sv.hrs_240
            precio = id_hh*horas
            return round(int(precio))
        elif 241<cc<500:
            horas = sv.hrs_500
            precio = id_hh*horas
            return round(int(precio))
        elif 501 <cc< 810:
            horas = sv.hrs_800
            precio = id_hh*horas
            return round(int(precio))
        elif cc > 810:
            horas = sv.hrs_810
            precio = id_hh*horas
            return round(int(precio))
        precio = 10000
        return precio
    if request.method == "POST":
        form2 = DetalleForm(request.POST)
        if form2.is_valid():
            form2.save(commit=False)
            datos = form2.cleaned_data
            detail = Detalle()
            detail.id_fi = ficha_id
            detail.id_sv = datos.get("id_sv")
            id_seleccionado = datos.get("id_sv")
            servicio_seleccionado = Servicio.objects.get(id = id_seleccionado.id)
            detail.precio_servicio = calculo(cc, servicio_seleccionado)
            detail.save()
            return redirect(detail_service, rut, patente, ficha)
        else:
            data["form"] = form2
    return render(request, "app/detail-service.html", data)

def delete_detail(request, id, rut, patente, ficha):
    detail = Detalle.objects.get(id=id)
    detail.delete()
    return redirect(detail_service, rut, patente, ficha)

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
    data_sv = Servicio.objects.all()
    list_id = []
    for data_id in data_sv:
        idsv = int(str(data_id.id).split("-")[1])
        list_id.append(idsv)
    max_id = max(list_id)
    new_id = max_id + 1
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
            if 'continue' in request.POST:
                service.save()
                return redirect(add_service)
            else:
                service.save()
                return redirect(list_services)
        else:
            data["form"] = form2
    
    return render(request, "app/add-service.html", data)

def generate_repair_order(request, rut, patente):
    form1 = OTForm(request.POST or None)
    form2 = Ficha_ingresoForm(request.POST or None)
    form3 = DetalleForm(request.POST or None)
    data = {
        "form1" : form1,
        "form2" : form2,
        "form3" : form3,
    }
    return render(request, "app/generate-repair-order.html", data)

def render_pdf_view(request, rut, patente, ficha):
    try:
        template_path = 'app/basespdf/ficha-ingreso-pdf.html'
        template = get_template(template_path)
        context = {'myvar': 'this is your template context'}
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)
        return response
    except:
        pass
    return redirect(dashboard)



# borrar
def ficha_ingreso(request, rut, patente):
    form = Ficha_ingresoForm(request.POST or None)
    data = {
        "form" : form, 
    }
    return render(request, "app/ficha-ingreso.html", data)