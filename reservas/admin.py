# reservas/admin.py
from django.contrib import admin
from .models import Recurso, Reserva

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'capacidade_maxima', 'localizacao', 'ativo')
    search_fields = ('nome', 'localizacao')
    list_filter = ('ativo', 'capacidade_maxima')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'usuario', 'data_hora_inicio', 'data_hora_fim', 'status')
    list_filter = ('status', 'recurso', 'data_hora_inicio')
    search_fields = ('motivo', 'usuario__username', 'recurso__nome')
    list_editable = ('status',)
    
    def save_model(self, request, obj, form, change):
        obj.save()