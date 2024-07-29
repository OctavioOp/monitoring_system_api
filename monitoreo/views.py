from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, viewsets, views
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializer import MaquinaProductivaSerializer, FallasSerializer, ReporteDiarioSerializer, ReporteMensualSerializer, UsuarioSerializer
from .models import maquinaProductiva, fallas, reporte_diario, reporte_mensual

# Obtén el modelo de usuario
Usuario = get_user_model()

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(f"Email: {email}, Password: {password}")  # Depuración
        try:
            user = Usuario.objects.get(email=email)
            print(f"User found: {user}")  # Depuración
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                print("Invalid password")  # Depuración
                return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except Usuario.DoesNotExist:
            print("User does not exist")  # Depuración
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class MaquinaProductivaViewSet(viewsets.ModelViewSet):
    queryset = maquinaProductiva.objects.all()
    serializer_class = MaquinaProductivaSerializer

class FallasViewSet(viewsets.ModelViewSet):
    queryset = fallas.objects.all()
    serializer_class = FallasSerializer

class ReporteDiarioViewSet(viewsets.ModelViewSet):
    queryset = reporte_diario.objects.all()
    serializer_class = ReporteDiarioSerializer

class ReporteMensualViewSet(viewsets.ModelViewSet):
    queryset = reporte_mensual.objects.all()
    serializer_class = ReporteMensualSerializer
