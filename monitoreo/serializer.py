from rest_framework import serializers
from .models import Usuario, maquinaProductiva, fallas, reporte_diario, reporte_mensual
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

Usuario = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'apellido', 'email', 'password', 'creado', 'cargo']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Usuario(
            email=validated_data['email'],
            rut=validated_data['rut'],
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            cargo=validated_data['cargo']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class MaquinaProductivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaProductiva
        fields = '__all__'

class FallasSerializer(serializers.ModelSerializer):
    class Meta:
        model = fallas
        fields = '__all__'

class ReporteDiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = reporte_diario
        fields = '__all__'

class ReporteMensualSerializer(serializers.ModelSerializer):
    class Meta:
        model = reporte_mensual
        fields = '__all__'
