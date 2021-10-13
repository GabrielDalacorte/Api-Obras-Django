from django.contrib import admin

# Register your models here.
from core.models import Obras, Autores


@admin.register(Autores)
class AutoresAdmin(admin.ModelAdmin):
    list_display = ['autores']


@admin.register(Obras)
class ObrasAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'editora', 'foto', 'autores']
