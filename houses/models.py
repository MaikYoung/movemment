from django.db import models


class House(models.Model):
    nombre_del_alojamiento = models.CharField(max_length=150, null=True, blank=True)
    habitaciones_descripcion = models.TextField(null=True, blank=True)
    banos_descripcion = models.TextField(null=True, blank=True)
    ubicacion = models.CharField(max_length=150, null=True, blank=True)
    ubicacion_url = models.URLField(blank=True, null=True)
    imagen_1 = models.URLField(blank=True, null=True)
    imagen_2 = models.URLField(blank=True, null=True)
    imagen_3 = models.URLField(blank=True, null=True)
    imagen_4 = models.URLField(blank=True, null=True)
    imagen_5 = models.URLField(blank=True, null=True)
    imagen_6 = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Alojamiento'
        verbose_name_plural = 'Alojamientos'
