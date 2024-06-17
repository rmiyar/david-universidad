from django.views.generic.list import ListView, View
from app.models import CursoMateria, EstudianteMateria, Estudiante, AuthUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .decorators import group_required
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

@method_decorator(group_required('ESTUDIANTES'), name='dispatch')
class ListaCursoMateria(ListView):
    model = CursoMateria
    template_name = 'curso_materia_list.html'
    context_object_name = 'cursos_materia'

    def get_queryset(self):
        # Obtener el usuario autenticado y el estudiante asociado
        auth_user = AuthUser.objects.get(id=self.request.user.id)
        estudiante = Estudiante.objects.get(usuario=auth_user)

        # Filtrar las materias que aún no ha seleccionado el estudiante
        materias_seleccionadas = EstudianteMateria.objects.filter(estudiante=estudiante).values_list('curso_materia__id_materia', flat=True)
        return CursoMateria.objects.exclude(id_materia__in=materias_seleccionadas)

class SeleccionarMateria(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        curso_id = request.POST.get('curso_id')
        
        try:
            # Obtener el usuario autenticado
            auth_user = AuthUser.objects.get(id=request.user.id)
            estudiante = Estudiante.objects.get(usuario=auth_user)
            curso_materia = CursoMateria.objects.get(id_materia=curso_id)
            
            # Crear la relación EstudianteMateria si no existe
            EstudianteMateria.objects.get_or_create(estudiante=estudiante, curso_materia=curso_materia)
            
        except ObjectDoesNotExist as e:
            # Manejar el caso donde el estudiante o curso no existen
            print(e)
            return redirect('error-page')  # Cambia esto a tu página de error o maneja el error de otra manera
        
        return redirect('lista-cursos-materia')  # Cambia esto a tu URL de éxito
