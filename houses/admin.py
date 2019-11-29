from django.contrib import admin

from houses.models import House


class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_del_alojamiento', 'ubicacion')
    search_fields = ('nombre_del_alojamiento', 'ubicacion')
    list_filter = ('ubicacion',)


admin.site.register(House, HouseAdmin)
