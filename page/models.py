from django.db import models
from django.core.validators import MaxLengthValidator

class HoraHombre(models.Model):
    nombre_hh = models.CharField(max_length=50)
    descripcion_hh= models.CharField(max_length=250, verbose_name="Descripción")
    precio_hh= models.PositiveIntegerField(verbose_name="Precio")
    
    def __str__(self):
        return self.nombre_hh
    
class Cliente(models.Model):
    rut_cli = models.CharField(primary_key=True, max_length=11, verbose_name="Rut")
    nombre_cli = models.CharField(max_length=50, verbose_name="Nombre")
    apellido_cli = models.CharField(max_length= 100, verbose_name="Apellido")
    direccion_clie = models.CharField(max_length=250, verbose_name="Dirección")
    celular_cli = models.IntegerField(verbose_name="Número contacto")
    
    def __str__(self):
        return self.rut_cli
    
class Vehiculo(models.Model):
    patente_vh= models.CharField(primary_key=True, max_length=7, verbose_name="Patente")
    marca_vh = models.CharField(max_length=50, verbose_name="Marca")
    cilindrada_vh = models.PositiveIntegerField( verbose_name="Cilindrada")
    kilometraje_vh = models.PositiveIntegerField( verbose_name="Kilometraje")
    rut_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Rut Cliente")
    
    def __str__(self):
        return self.patente_vh
    
class Servicio(models.Model):
    nombre_sv = models.CharField(max_length=50, verbose_name= "Nombre Servicio")
    desc_sv = models.CharField(max_length=250, verbose_name= "Descripción Servicio")
    hrs_240 = models.PositiveIntegerField( verbose_name="Valor < 240 cc")
    hrs_500 = models.PositiveIntegerField( verbose_name="Valor < 500 cc")
    hrs_800 = models.PositiveIntegerField( verbose_name="Valor < 800 cc")
    hrs_810 = models.PositiveIntegerField( verbose_name="Valor > 810 cc")
    id_hh = models.ForeignKey(HoraHombre, verbose_name= "ID Hora Hombre", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_sv
    
class Ficha_ingreso(models.Model):
    fecha_ing_fi= models.DateField(auto_now_add=True, verbose_name="Fecha Ingreso")
    total_fi= models.PositiveIntegerField(verbose_name="Total")
    observaciones_fi= models.CharField(max_length=250, verbose_name="Observaciones")
    patente_vh = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name="Patente")
    rut_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Rut")
    estado_fi = models.CharField(max_length=50, verbose_name="Estado")
    
    def __str__(self):
        return str(self.patente_vh)
    
class Detalle(models.Model):
    precio_servicio = models.PositiveIntegerField( verbose_name="Precio servicio")
    id_fi = models.ForeignKey(Ficha_ingreso, on_delete=models.CASCADE, verbose_name="Número de Ficha")
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
    rut_trab = models.CharField(primary_key=True, verbose_name="Rut", max_length=11)
    nombre_trab = models.CharField(max_length=50, verbose_name="Nombre")
    apellido_trab_pa = models.CharField(max_length= 100, verbose_name="Apellido Paterno")
    apellido_trab_ma = models.CharField(max_length= 100, verbose_name="Apellido Materno")
    celular_trab = models.IntegerField(verbose_name="Número Contacto", validators=[MaxLengthValidator(999999999)])
    tipo_trab = models.CharField(max_length=20, verbose_name="Clasificación")
    
    def __str__(self):
        return self.rut_trab
    
class Orden_trabajo(models.Model):
    fecha_ing_ot = models.DateField(auto_now_add=True, verbose_name="Fecha Ingreso")
    fecha_fin_ot = models.DateField(auto_now=False, verbose_name="Fecha Finalización", null=True, blank=True)
    id_fi = models.ForeignKey(Ficha_ingreso, on_delete=models.CASCADE, verbose_name="Ficha Ingreso" )
    rut_trab = models.ForeignKey(Trabajador, on_delete=models.CASCADE, verbose_name="Trabajador")
    
    def __str__(self):
        return str(self.id_fi)
    

class Falla(models.Model):
    nombre_f = models.CharField(max_length=50, verbose_name="Nombre Falla")
    desc_f = models.CharField(max_length=250, verbose_name="Descripción Falla")
    hora_hh_f = models.IntegerField( verbose_name="Horas Hombre", validators=[MaxLengthValidator(9999)])
    id_ot = models.ForeignKey(Orden_trabajo, models.CASCADE, verbose_name="Orden Trabajo")
    
    def __str__(self):
        return self.nombre_f
    
    
    

    
    
    
    
        
    
