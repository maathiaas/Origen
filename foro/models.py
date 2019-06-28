from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(
        default=timezone.now)
    fecha_publicacion = models.DateTimeField(
        blank=True, null=True, default=timezone.now)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

    def comentarios_aprobado(self):
        return self.comentarios.filter(comentario_aprobado=True)


class Comentario(models.Model):
    post = models.ForeignKey(
        'foro.Post', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    comentario_aprobado = models.BooleanField(default=False)

    def aprobar(self):
        self.comentario_aprobado = True
        self.save()

    def __str__(self):
        return self.texto
