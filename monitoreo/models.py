from django.db import models

# Create your models here.
class usuario(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    cargo = models.CharField(max_length=50)

class maquinaProductiva(models.Model):
    id_maquina = models.CharField(max_length=50)
    nombre_maquina = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fabricante = models.TextField()
    capacidad_produccion = models.FloatField()
    potencia = models.FloatField()
    operador = models.ForeignKey(usuario,on_delete=models.CASCADE, related_name='operador')


class fallas(models.Model):
    maquina = models.ForeignKey(maquinaProductiva, on_delete=models.CASCADE, related_name="maquina_fallas")
    fecha_inicio = models.DateTimeField(auto_now=False, auto_now_add=True)
    tiempo_falla = models.BigIntegerField()
    descripcion = models.TextField()
    gravedad = models.CharField(max_length=50)


class reporte_diario(models.Model):
    maquina = models.ForeignKey(maquinaProductiva, verbose_name=("reporte_maquina"), on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)
    produccion_total = models.IntegerField()
    produccion_defectuosa = models.FloatField()
    tasa_defectuosa = models.BigIntegerField()
    tiempo_operacion = models.BigIntegerField()
    tiempo_inactividad = models.BigIntegerField()
    calidad = models.FloatField()
    oee = models.FloatField()


class reporte_mensual(models.Model):
    maquina = models.ForeignKey(maquinaProductiva, verbose_name=("reporte_maquina_mensual"), on_delete=models.CASCADE)
    fecha_creacion_mensual = models.DateField(auto_now=False, auto_now_add=True)
    produccion_total_mensual = models.IntegerField()
    produccion_defectuosa_mensual = models.FloatField()
    tasa_defectuosa_mensual = models.BigIntegerField()
    tiempo_operacion_mensual = models.BigIntegerField()
    tiempo_inactividad_mensual = models.BigIntegerField()
    calidad_mensual = models.FloatField()
    oee_mensual = models.FloatField()
