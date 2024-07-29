from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser):
    rut = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    creado = models.DateTimeField(auto_now_add=True)
    cargo = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut', 'nombre', 'apellido', 'cargo']

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class maquinaProductiva(models.Model):
    id_maquina = models.CharField(max_length=50, unique=True)
    nombre_maquina = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fabricante = models.TextField()
    capacidad_produccion = models.FloatField()
    potencia = models.FloatField()
    operador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='operador')

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
