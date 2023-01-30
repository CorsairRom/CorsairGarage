from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import HoraHombre,Cliente, Detalle,Falla,Ficha_ingreso,Insumos,Orden_trabajo,Servicio,\
                    Trabajador,Vehiculo

class H_HForm(forms.ModelForm):
    
    class Meta:
        model = HoraHombre
        fields = '__all__'

class ServicioForm(forms.ModelForm):
    
    class Meta:
        model = Servicio
        fields = '__all__'
        
class DetalleForm(forms.ModelForm):
    
    class Meta:
        model = Detalle
        fields = '__all__'
        
class Ficha_ingresoForm(forms.ModelForm):
    
    class Meta:
        model = Ficha_ingreso
        fields = '__all__'
        
class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'
        exclude = ('usuario_cli',)
        
class FallaForm(forms.ModelForm):
    
    class Meta:
        model = Falla
        fields = '__all__'
        
class InsumosForm(forms.ModelForm):
    
    class Meta:
        model = Insumos
        fields = '__all__'
        
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
    

class TrabajadorForm(forms.ModelForm):
    
    class Meta:
        model = Trabajador
        fields = '__all__'
        