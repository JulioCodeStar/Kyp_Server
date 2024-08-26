from .models import Pacientes
from .serializers import PacienteSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PacienteViews(ModelViewSet):
    queryset = Pacientes.objects.all()
    serializer_class = PacienteSerializer
    # permission_classes = [IsAuthenticated]