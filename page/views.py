import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente, Detalle, Ficha_ingreso, HoraHombre, Vehiculo, Servicio, Insumos
from .forms import ClienteForm, DetalleForm, Ficha_ingresoForm, OTForm, ServicioForm, VehiculoForm, buscarRut, Vehiculo_change_kmForm, Form_login,InsumosForm
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from dotenv import load_dotenv
import json


# ----------------PAGE SECTION!--------------------------------

def index(request):
    data ={
        'GOOGLE_MAPS_API_KEY': os.getenv('GOOGLE_MAPS_API_KEY')
    }
    
    return render(request, "page/index.html", data)

def sign_in(request):
    data ={
        "form" : Form_login()
    }
    if request.method =='POST':
        form = Form_login(request, data = request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = name_user, password = password)
            if user is not None:
                login(request, user)
                return redirect(dashboard)
    return render(request, 'registration/login.html', data)

def log_out(request):
    logout(request)
    return redirect(index)

# ----------------APP SECTION!--------------------------------
@login_required()
def dashboard(request):
    if request.method == 'GET':
        patente = request.GET.get('buscarPatente', None)
        if patente is not None and len(patente) > 4:
           data = Vehiculo.objects.get(patente_vh=patente)
           rut = str(data.rut_cli)
           return redirect(view_bikes_client, rut)
        
    return render(request, "app/dashboard.html")

#funcionando
@login_required()
def consulta_cliente(request, rut2):
    form = ClienteForm (request.POST or None, initial={'rut_cli': rut2})
    data = {
        "form" : form   
    } 
    if request.method == "POST":
        form = ClienteForm(data = request.POST)
        
        if form.is_valid():
            form.save(commit=False)
            datos = form.cleaned_data
            client = Cliente()
            rut = datos.get("rut_cli")
            client.rut_cli = rut
            client.nombre_cli = datos.get("nombre_cli")
            client.apellido_cli = datos.get("apellido_cli")
            client.direccion_clie = datos.get("direccion_clie")
            client.celular_cli = datos.get("celular_cli")
            client.save()
            # print('--------------------')
            # print(rut)
            return redirect(add_Mbike, rut)   
        else:
            # print('invalido el form')
            return render(request, "app/create-cliente.html", {"form": form})
    return render(request, "app/create-cliente.html", data)


#---------------------API SECTION!--------------------
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
#---------------------fin api--------------------

# @login_required()
#----------------------borrar-------------
# def create_client(request, rut2):
#     form = ClienteForm (request.POST or None, initial={'rut': rut2})
#     data = {
#         "form" : form
#     }
#     if request.method == "POST":
#         form2 = ClienteForm(request.POST)
#         if form2.is_valid():
#             form2.save(commit=False)
#             datos = form2.cleaned_data
#             client = Cliente()
#             rut = datos.get("rut_cli")
#             client.rut_cli = rut
#             client.nombre_cli = datos.get("nombre_cli")
#             client.apellido_cli = datos.get("apellido_cli")
#             client.direccion_clie = datos.get("direccion_clie")
#             client.celular_cli = datos.get("celular_cli")
#             client.save()
#             print(rut)
#             return redirect(add_Mbike, rut)
#             #aqui falta el return render para que no se duplique
#         else:
#             return render(request, "page/create-client.html", {"form": form2})   
#     return render(request, "app/create-client.html", data)

@login_required()
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

@login_required()
def detail_service(request, rut, patente, ficha):
    form = DetalleForm(request.POST or None, initial={'id_fi': ficha})
    ficha_id = Ficha_ingreso.objects.get(id=ficha)
    detalles = Detalle.objects.filter(id_fi = ficha)
    Mbikes = Vehiculo.objects.get(patente_vh = patente)
    client = Cliente.objects.get(rut_cli = rut)
    insumosForm = InsumosForm(request.POST or None, initial={'id_fi':ficha})
    insumos = Insumos.objects.filter(id_fi = ficha)
    total = 0
    totalFin = 0
    desc = 0
    totInsumos = 0
    if insumos:
        for insTotal in insumos:
            totInsumos += insTotal.precio_total 
    
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
        "desc": desc,
        "insumosForm" : insumosForm,
        "insumos" : insumos,
        "totalInsumos" : totInsumos
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
    if request.method == "POST" and 'addServices' in request.POST:
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
    if request.method == "POST" and 'addSpare' in request.POST:
        formIns = InsumosForm(request.POST)
        if formIns.is_valid():
            formIns.save(commit=False)
            dataIns = formIns.cleaned_data
            ins = Insumos()
            ins.codigo_is_externo = dataIns.get("codigo_is_externo")
            ins.nombre_is = dataIns.get("nombre_is")
            ins.cantidad_is = dataIns.get("cantidad_is")
            ins.precio_is_unitario = dataIns.get("precio_is_unitario")
            ins.precio_total = dataIns.get("precio_is_unitario") * dataIns.get("cantidad_is")
            ins.id_fi = ficha_id
            ins.save()
            return redirect(detail_service, rut, patente, ficha)
        else:
            data["insumosForm"] = formIns
        
    return render(request, "app/detail-service.html", data)


# ---------------delete section----------------
@login_required()
def delete_detail(request, id, rut, patente, ficha):
    detail = Detalle.objects.get(id=id)
    detail.delete()
    return redirect(detail_service, rut, patente, ficha)

@login_required()
def delete_spare(reques, id, rut, patente, ficha):
    spare = Insumos.objects.get(id=id)
    spare.delete()
    return redirect(detail_service, rut, patente, ficha)

@login_required()
def add_Mbike(request, rut):
    form = VehiculoForm(request.POST or None, initial={'rut_cli': rut})
    data = {
        "form" : form
    }
        
    if request.method == "POST":
        form2 = VehiculoForm(data = request.POST)
        if form.is_valid():
            form.save(commit=False)
            datos = form.cleaned_data
            Mbike = Vehiculo()
            Mbike.patente_vh = datos.get("patente_vh")
            Mbike.marca_vh = datos.get("marca_vh")
            Mbike.modelo_vh = datos.get("modelo_vh")
            Mbike.cilindrada_vh = datos.get("cilindrada_vh")
            Mbike.kilometraje_vh = datos.get("kilometraje_vh")
            Mbike.rut_cli = datos.get("rut_cli")
            Mbike.save()
            return redirect(view_bikes_client, rut)
        else:
            data["form"] = form2
    return render(request, "app/add-Mbike.html", data)

@login_required()
def list_services(request):
    services = Servicio.objects.all()
    data = {
        "services": services
    }
    return render(request, "app/list-services.html", data)

@login_required()
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

@login_required()
def list_repair_order(request):
    
    fichas = Ficha_ingreso.objects.all()
    data = {
        "fichas" : fichas
    }
    return render(request, "app/list-repair-order.html", data)

@login_required()
def render_pdf_view(request, rut, patente, ficha_id, desc, total, totalFinal):
    ficha = Ficha_ingreso.objects.get(id=ficha_id)
    client = Cliente.objects.get(rut_cli = rut)
    detail = Detalle.objects.filter(id_fi= ficha_id)
    bike = Vehiculo.objects.get(patente_vh = patente)
    insumos = Insumos.objects.filter(id_fi= ficha_id)
    
    totalInsumos = 0
    if insumos:
        for i in insumos:
            totalInsumos += i.precio_total
          
    calc_desc = 0
    if desc > 0:
        calc_desc = round(((total*desc)/100))
    
    try:
        template_path = 'app/basespdf/ficha-ingreso-pdf.html'
        template = get_template(template_path)
        context = {
            'rut': rut,
            'patente': patente,
            'ficha': ficha,
            'desc': desc,
            'total': total,
            'totalFinal' : totalFinal,
            'client' : client,
            'detail' : detail,
            'valorDesc': calc_desc,
            'bike' : bike,
            'insumos' : insumos,
            'totalInsumos' : totalInsumos
            
        }
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = f'attachment; filename="{rut}_{patente}_{ficha_id}.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)
        return response
    except:
        pass
    return redirect(dashboard)

def list_client(request):
    clientes = Cliente.objects.all()
    data = {
        'clientes' : clientes
    }
    return render(request, "app/list-client.html", data )

def list_motos(request):
    motos = Vehiculo.objects.all()
    data = {
        'motos' : motos
    }
    return render(request, "app/list-bike.html", data)



def valve_service(request):
    
    return render(request,'app/valve-service.html')

# borrar
def ficha_ingreso(request, rut, patente):
    form = Ficha_ingresoForm(request.POST or None)
    data = {
        "form" : form, 
    }
    return render(request, "app/ficha-ingreso.html", data)