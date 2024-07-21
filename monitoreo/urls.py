from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from monitoreo import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.usuarioView,basename='usuarios')
router.register(r'maquinas', views.maquinaView,basename='maquinas')
router.register(r'fallas',views.fallaView,basename='fallas')
router.register(r'reporte_diario', views.reporteDiarioView,basename='reporte_diario')
router.register(r'reporte_mensual', views.reporteMensualView, basename='reporte_mensual')


urlpatterns = [
    path("api/v1/", include(router.urls)),
     path('docs/',include_docs_urls(title='monitoreo api'))
   
]
