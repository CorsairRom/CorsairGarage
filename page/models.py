from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User


unidad_medida = [
    ('km', 'Kilometros'),
    ('mill', 'Millas'),
]

opcion_tipo_sv = [
    ('Mantencion', 'Mantención'),
    ('Ajuste', 'Ajuste'),
    ('Reemplazo', 'Reemplazo'),
    ('Reparacion', 'Reparación'), 
    ('Modificacion', 'Modificación'), 
    ('Revision', 'Revisión'), 
]

class HoraHombre(models.Model):
    nombre_hh = models.CharField(max_length=50)
    descripcion_hh= models.CharField(max_length=250, verbose_name="Descripción")
    precio_hh= models.PositiveIntegerField(verbose_name="Precio")
    
    def __str__(self):
        return self.nombre_hh + ' $' + str(self.precio_hh)
    
class Cliente(models.Model):
    usuario_cli = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario", null=True)
    rut_cli = models.CharField(primary_key=True, max_length=11, verbose_name="Rut")
    nombre_cli = models.CharField(max_length=50, verbose_name="Nombre")
    apellido_cli = models.CharField(max_length= 100, verbose_name="Apellido")
    direccion_clie = models.CharField(max_length=250, verbose_name="Dirección")
    celular_cli = models.IntegerField(verbose_name="Número contacto")
    
    def __str__(self):
        return self.rut_cli
    
class Vehiculo(models.Model):
    rut_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Rut Cliente")
    patente_vh= models.CharField(primary_key=True, max_length=7, verbose_name="Patente")
    marca_vh = models.CharField(max_length=50, verbose_name="Marca")
    modelo_vh = models.CharField(max_length=50, verbose_name="Modelo")
    cilindrada_vh = models.PositiveIntegerField( verbose_name="Cilindrada")
    kilometraje_vh = models.PositiveIntegerField( verbose_name="Kilometraje")
    mill_km_vh = models.CharField(max_length=50, verbose_name="Unidad de Medida", choices=unidad_medida, default='Kilometros')
    
    def __str__(self):
        return self.patente_vh
    
class Servicio(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    nombre_sv = models.CharField(max_length=50, verbose_name= "Nombre Servicio")
    desc_sv = models.TextField(verbose_name= "Descripción Servicio")
    hrs_240 = models.FloatField( verbose_name="Horas hasta 240 cc")
    hrs_500 = models.FloatField( verbose_name="Horas hasta 500 cc")
    hrs_800 = models.FloatField( verbose_name="Horas hasta 800 cc")
    hrs_810 = models.FloatField( verbose_name="Horas desde 810 cc")
    tipo_sv = models.CharField(max_length=250 ,verbose_name= "Tipo Servicio", choices=opcion_tipo_sv, default='Mantención')
    id_hh = models.ForeignKey(HoraHombre, verbose_name= "ID Hora Hombre", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_sv
    
class Ficha_ingreso(models.Model):
    patente_vh = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name="Patente")
    rut_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Rut")
    fecha_ing_fi= models.DateField(auto_now_add=True, verbose_name="Fecha Ingreso")
    observaciones_fi= models.TextField(verbose_name="Observaciones")
    
    def __str__(self):
        return str(self.id) #type: ignore
    
class Detalle(models.Model):
    precio_servicio = models.PositiveIntegerField( verbose_name="Precio servicio")
    id_fi = models.ForeignKey(Ficha_ingreso, on_delete=models.CASCADE, verbose_name="Número de Ficha", null=True, blank=True)
    id_sv = models.ForeignKey(Servicio, on_delete=models.CASCADE, verbose_name="Número de servicio")
    
    def __str__(self):
        return str(self.id_fi)

class Insumos(models.Model):
    nombre_is = models.CharField(max_length=50, verbose_name="Nombre Insumo")
    cantidad_is = models.PositiveIntegerField( verbose_name="Cantidad")
    id_fi = models.ForeignKey(Ficha_ingreso, on_delete=models.CASCADE, verbose_name="Id Ficha")
    
    def __str__(self):
        return self.nombre_is

class Trabajador(models.Model):
    usuario_trab = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    rut_trab = models.CharField(primary_key=True, verbose_name="Rut", max_length=11)
    nombre_trab = models.CharField(max_length=50, verbose_name="Nombre")
    apellido_trab_pa = models.CharField(max_length= 100, verbose_name="Apellido Paterno")
    apellido_trab_ma = models.CharField(max_length= 100, verbose_name="Apellido Materno")
    celular_trab = models.IntegerField(verbose_name="Número Contacto")
    tipo_trab = models.CharField(max_length=250, verbose_name="Clasificación")
    
    def __str__(self):
        return  self.nombre_trab + ' ' + self.apellido_trab_pa + ' ' +self.rut_trab
    
class Orden_trabajo(models.Model):
    fecha_ing_ot = models.DateField(auto_now_add=True, verbose_name="Fecha Ingreso")
    fecha_fin_ot = models.DateField(auto_now=False, verbose_name="Fecha Finalización", null=True, blank=True)
    id_fi = models.ForeignKey(Ficha_ingreso, on_delete=models.CASCADE, verbose_name="Ficha Ingreso" )
    rut_trab = models.ForeignKey(Trabajador, on_delete=models.CASCADE, verbose_name="Trabajador")
    total_fi= models.PositiveIntegerField(verbose_name="Total", default=0)
    def __str__(self):
        return str(self.id_fi)
    

class Falla(models.Model):
    nombre_f = models.CharField(max_length=50, verbose_name="Nombre Falla")
    desc_f = models.CharField(max_length=250, verbose_name="Descripción Falla")
    hora_hh_f = models.IntegerField( verbose_name="Horas Hombre")
    id_ot = models.ForeignKey(Orden_trabajo, models.CASCADE, verbose_name="Orden Trabajo")
    
    def __str__(self):
        return self.nombre_f
    
    
    

    
    
    
    
        
    
