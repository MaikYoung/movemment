from django.db import models


class Teacher(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    imagen_url = models.URLField(blank=True, null=True)
    especialidad_de_yoga = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'


