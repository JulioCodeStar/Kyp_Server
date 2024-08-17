from .models import Pacientes
from rest_framework.serializers import ModelSerializer

class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'