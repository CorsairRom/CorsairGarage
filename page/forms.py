from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import HoraHombre,Cliente, Detalle,Falla,Ficha_ingreso,Insumos,Orden_trabajo,Servicio,\
                    Trabajador,Vehiculo
from page.Rut import validarRut
from django.core.exceptions import ValidationError



class query_rut(forms.ModelForm):
    rut = forms.CharField(max_length=12)
    
    def clean(self):
        super(query_rut, self).clean()
        ruts = self.cleaned_data.get('rut_cli')
        if  validarRut(str(ruts)) == False:
            self.errors['rut_cli'] = self.error_class(['Rut Inválido'])
        return self.cleaned_data


class Form_login(AuthenticationForm):
    
    class Meta:
        model = User
        field = ['username', 'password',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields['username'].label = 'Usuario'   
        self.fields['password'].label = 'Contraseña'  


class H_HForm(forms.ModelForm):
    
    class Meta:
        model = HoraHombre
        fields = '__all__'

class ServicioForm(forms.ModelForm):
    
    class Meta:
        model = Servicio
        fields = '__all__'
        exclude = ('id',)
        
class DetalleForm(forms.ModelForm):
    
    class Meta:
        model = Detalle
        fields = '__all__'
        exclude = ('precio_servicio', 'id_fi')
        
class Ficha_ingresoForm(forms.ModelForm):
    
    class Meta:
        model = Ficha_ingreso
        fields = '__all__'
        exclude = ('rut_cli',)
        
class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'
        exclude = ('usuario_cli',)
        help_texts = {
            'rut': ('Formato 12.345.678-9.'),
        }
        
    def clean(self):
        super(ClienteForm, self).clean()
        ruts = self.cleaned_data.get('rut_cli')
        if  validarRut(str(ruts)) == False:
            self.errors['rut_cli'] = self.error_class(['Rut Inválido'])
        return self.cleaned_data    
        
class FallaForm(forms.ModelForm):
    
    class Meta:
        model = Falla
        fields = '__all__'
        
class InsumosForm(forms.ModelForm):
    
    class Meta:
        model = Insumos
        fields = '__all__'
        exclude = ('id_fi','precio_total')
        
class OTForm(forms.ModelForm):
    
    class Meta:
        model = Orden_trabajo
        fields = '__all__'

class VehiculoForm(forms.ModelForm):
    
    class Meta:
        model = Vehiculo
        fields = '__all__'
        
    def clean_patente_vh(self):
        data = self.cleaned_data['patente_vh']
        return data.upper()
    
    def clean_marca_vh(self):
        data = self.cleaned_data['marca_vh']
        return data.upper()
    
    def clean_modelo_vh(self):
        data = self.cleaned_data['modelo_vh']
        return data.upper()
class Vehiculo_change_kmForm(forms.ModelForm):
    
    class Meta:
        model = Vehiculo
        fields = ['kilometraje_vh',]
    

class TrabajadorForm(forms.ModelForm):
    
    class Meta:
        model = Trabajador
        fields = '__all__'
        
class buscarRut(forms.ModelForm):
    
    rut = forms.CharField(max_length=10)
        