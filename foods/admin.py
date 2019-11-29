from django.contrib import admin

from foods.models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_vegetariano', 'menu_carnivoro')
    search_fields = ('id',)


admin.site.register(Food, FoodAdmin)
