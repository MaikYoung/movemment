from django.contrib import admin
from django.contrib.auth.models import User, Group

from houses.models import House


class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_del_alojamiento', 'ubicacion')
    search_fields = ('nombre_del_alojamiento', 'ubicacion')
    list_filter = ('ubicacion',)


admin.site.register(House, HouseAdmin)

#admin users
admin.site.unregister(User)
admin.site.unregister(Group)
