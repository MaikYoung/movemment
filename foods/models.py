from django.db import models


class Food(models.Model):
    menu_vegetariano = models.TextField(blank=True, null=True)
    menu_carnivoro = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Comida'
        verbose_name_plural = 'Comidas'
