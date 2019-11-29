from django.contrib import admin

from events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('titulo_evento', 'fecha_inicio', 'fecha_fin', 'activo', 'lleno')
    search_fields = ('titulo_evento', )
    list_filter = ('activo', 'lleno', 'localizacion_evento')


admin.site.register(Event, EventAdmin)
