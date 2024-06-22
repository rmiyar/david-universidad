from django.contrib import admin
from app.models import Estudiante, Profesor, Curso, CursoMateria,PagosMetodo
from django.db import IntegrityError
from django.contrib import messages
from django.core.exceptions import ValidationError



class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id_estudiante','nombre', 'apellido','cedula','telefono','direccion', 'email','usuario')
    search_fields = ('id_estudiante','nombre', 'apellido')
    readonly_fields = ('id_estudiante',)
    
    def listar_materias(self, obj):
        return ", ".join([m.nombre for m in obj.materias.all()])
    listar_materias.short_description = 'Materias'
    
    def save_model(self, request, obj, form, change):
        try:
            obj.clean()  # Llama al método clean() del modelo
            super().save_model(request, obj, form, change)
        except ValidationError as e:
            self.message_user(request, e.message, level=messages.ERROR)

# Registrando con la clase personalizada
admin.site.register(Estudiante, EstudianteAdmin)

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('id_profesor','nombre', 'apellido','cedula','telefono','direccion', 'email','id_historial','id_materia','usuario')
    search_fields = ('id_profesor','nombre', 'apellido')
    readonly_fields = ('id_profesor',)
    
    def save_model(self, request, obj, form, change):
        try:
            obj.clean()  # Llama al método clean() del modelo
            super().save_model(request, obj, form, change)
        except ValidationError as e:
            self.message_user(request, e.message, level=messages.ERROR)


admin.site.register(Profesor, ProfesorAdmin)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id_curso','creditos', 'plazas_disponibles','nivel_academico','id_materia')
    search_fields = ('id_curso','creditos', 'plazas_disponibles','nivel_academico','id_materia')
    readonly_fields = ('id_curso',)

admin.site.register(Curso, CursoAdmin)


class CursoMateriaAdmin(admin.ModelAdmin):
    list_display = ('id_materia','materia', 'codigo_curso','plan_estudio','requisitos_previos','instrumentos')
    search_fields = ('id_materia','materia', 'codigo_curso','plan_estudio','requisitos_previos','instrumentos')
    readonly_fields = ('id_materia',)

admin.site.register(CursoMateria, CursoMateriaAdmin)



class PagosMetodoAdmin(admin.ModelAdmin):
    list_display = ('id_metodo_pago','tipo_pago')
    search_fields = ('id_metodo_pago','tipo_pago')
    readonly_fields = ('id_metodo_pago',)

admin.site.register(PagosMetodo, PagosMetodoAdmin)
