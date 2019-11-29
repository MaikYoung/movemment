from django.db import models


class Event(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    titulo_evento = models.CharField(max_length=150)
    descripcion_evento = models.TextField()
    localizacion_evento = models.CharField(max_length=150)
    profesores_fk = models.CharField(max_length=150)
    alojamiento_fk = models.CharField(max_length=150)
    comida_fk = models.CharField(max_length=150)
    instrucciones_como_llegar = models.TextField()
    limite_usuarios = models.IntegerField()
    usuarios_que_van = models.IntegerField(default=0)
    a_quien_va_dirigido = models.TextField()
    donde_es_como_llego = models.TextField()
    que_aprenderas = models.TextField()
    cual_es_horario = models.TextField()
    que_necesitas_traer = models.TextField()
    quien_dara_clases = models.TextField()
    que_te_proporcionamos = models.TextField()
    lleno = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
