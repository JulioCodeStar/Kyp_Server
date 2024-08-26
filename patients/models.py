from django.db import models

# Create your models here.
class Pacientes(models.Model):
    id_paciente     = models.CharField(max_length=10, null=False, blank=False)
    dni             = models.IntegerField(max_length=20, null=False)
    nombres         = models.CharField(max_length=200, null=False, blank=False)
    apellidos       = models.CharField(max_length=200, null=False, blank=False)
    genero          = models.CharField(max_length=50, null=False, blank=False)
    celular         = models.CharField(max_length=20, null=False, blank=False)
    otro_contact    = models.CharField(max_length=20, null=False, blank=False)
    direccion       = models.CharField(max_length=255, null=False, blank=False)
    locacion        = models.CharField(max_length=100, null=False, blank=False)
    edad            = models.IntegerField(max_length=3, null=False)
    sede            = models.CharField(max_length=50, null=False, blank=False)
    estado          = models.CharField(max_length=100, null=False, blank=False)
    time_ampu       = models.CharField(max_length=255, null=False, blank=False)
    motivo          = models.CharField(max_length=255, null=False, blank=False)
    canal           = models.CharField(max_length=100, null=False, blank=False)
    observacion     = models.TextField(null=True, blank=True)
    fecha_nac       = models.DateField(null=False, blank=False)
    email_pat       = models.EmailField(null=True, blank=True)
    afecciones      = models.CharField(max_length=100, null=True, blank=True)
    alergias        = models.CharField(max_length=100, null=True, blank=True)
    vendedor        = models.CharField(max_length=255, null=False, blank=False)
    
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "kyp_pacientes"