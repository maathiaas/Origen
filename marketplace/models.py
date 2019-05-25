from django.contrib.auth.models import User
from django.db import models

class RegistroUsuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    correo = models.EmailField(max_length=30)
    usuario = models.CharField(max_length = 15)
    contraseña = models.CharField(max_length= 20)
    def __str__ (self):
        return self.nombre