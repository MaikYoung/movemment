from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellidos', 'email', 'telefono')
    search_fields = ('id', 'nombre', 'apellidos', 'email')


admin.site.register(Teacher, TeacherAdmin)
