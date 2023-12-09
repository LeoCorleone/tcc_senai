# admin.py
from django.contrib import admin
from .models import PaginaAjuda

@admin.register(PaginaAjuda)
class PaginaAjudaAdmin(admin.ModelAdmin):
    list_display = ('pagina',)
