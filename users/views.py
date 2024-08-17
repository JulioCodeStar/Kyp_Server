from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import UsersModel

# Create your views here.
class UserRegisterView(ModelViewSet):
    queryset = UsersModel.objects.all()  # Define el conjunto de datos
    serializer_class = UserSerializer  # Asigna el serializador