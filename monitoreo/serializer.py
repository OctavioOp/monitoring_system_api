from .models import usuario, maquinaProductiva, fallas,reporte_diario, reporte_mensual
from rest_framework  import serializers



class usuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model= usuario
        field= ('id', 'nombre','apellido','email','password','creado','cargo')


class maquinaProductivaSerializer(serializers.ModelSerializer):
    class Meta:
        model= maquinaProductiva
        field= ('id','id_maquina','nombre_maquina','descripcion','fabricante','capacidad_produccion','potencia','operador')


class fallasSerializer(serializers.ModelSerializer):
    class Meta:
        model= fallas
        field = ('id', 'maquina', 'fecha_inicio', 'tiempo_falla', 'descripcion', 'gravedad')

class reporte_diarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= reporte_diario
        field= ('id','maquina','fecha_creacion','produccion_total','produccion_defectuosa', 'tasa_defectuosa', 'tiempo_operacion', 'tiempo_inactividad', 'calidad', 'oee')


class reporte_mensualSerializer(serializers.ModelSerializer):
    class Meta:
        model = reporte_mensual
        field= ('id','maquina','fecha_creacion_mensual','produccion_total_mensual','produccion_defectuosa_mensual', 'tasa_defectuosa_mensual', 'tiempo_operacion_mensual', 'tiempo_inactividad_mensual', 'calidad_mensual', 'oee_mensual')