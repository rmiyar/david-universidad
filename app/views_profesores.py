from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from .models import AuthUser, EstudianteMateria, Profesor
from django.views.generic import ListView


class PerfilProfesorView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            # Obtener el usuario autenticado
            auth_user = AuthUser.objects.get(id=request.user.id)
            print(auth_user)
            profesor = Profesor.objects.get(usuario=auth_user)
            print(profesor)
        except ObjectDoesNotExist:
            # Redireccionar a una página de error si no se encuentra la información
            return redirect('error-page')

        # Renderizar la página con la información del profesor
        return render(request, 'perfil.html', {
            'profesor': profesor,
        })
        
        
        
class EstudiantesMateriaView(LoginRequiredMixin, ListView):
    template_name = 'estudiantes_materia.html'
    context_object_name = 'estudiantes'

    def get_queryset(self):
        # Obtener el usuario autenticado
        auth_user = AuthUser.objects.get(id=self.request.user.id)
        profesor = Profesor.objects.get(usuario=auth_user)
    
        # Obtener la materia del profesor
        materia = profesor.id_materia
        
        # Obtener los estudiantes vinculados a la materia del profesor
        estudiantes_materia = EstudianteMateria.objects.filter(curso_materia=materia).select_related('estudiante')
        
        # Devolver la lista de estudiantes
        return [em.estudiante for em in estudiantes_materia]        