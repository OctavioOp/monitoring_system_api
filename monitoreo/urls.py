from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from . import views  # Usa esta importación para evitar problemas
from .views import LoginView

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet, basename='usuario')
router.register(r'maquinaProductiva', views.MaquinaProductivaViewSet, basename='maquinaProductiva')
router.register(r'fallas', views.FallasViewSet, basename='fallas')
router.register(r'reporte_diario', views.ReporteDiarioViewSet, basename='reporte_diario')
router.register(r'reporte_mensual', views.ReporteMensualViewSet, basename='reporte_mensual')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('api/login/', LoginView.as_view(), name='login'),
    path('docs/', include_docs_urls(title='monitoreo api'))
]
