from django.shortcuts import render
from rest_framework import viewsets
from .serializer import usuarioSerializer, maquinaProductiva, fallasSerializer, reporte_diarioSerializer, reporte_mensualSerializer
from .models import usuario, maquinaProductiva, fallas,reporte_diario,reporte_mensual


# Create your views here.


class usuarioView(viewsets.ModelViewSet):
    serializer_class= usuarioSerializer
    queryset = usuario.objects.all()

class maquinaView(viewsets.ModelViewSet):
    serializer_class= maquinaProductiva
    queryset= maquinaProductiva.objects.all()

class fallaView(viewsets.ModelViewSet):
    serializer_class= fallasSerializer
    queryset = fallas.objects.all()

class reporteDiarioView(viewsets.ModelViewSet):
    serializer_class = reporte_diarioSerializer
    queryset = reporte_diario.objects.all()

class reporteMensualView(viewsets.ModelViewSet):
    serializer_class: reporte_mensualSerializer
    queryset = reporte_mensual.objects.all()