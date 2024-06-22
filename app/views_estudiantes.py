
from django.utils import timezone
from django.views.generic.list import ListView, View
from app.models import CursoMateria, EstudianteMateria, Estudiante, AuthUser,PagosMetodo,Pagos, PagosMetodo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .decorators import group_required
from django.shortcuts import render, redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse


@method_decorator(group_required('ESTUDIANTES'), name='dispatch')
class ListaCursoMateria(ListView):
    model = CursoMateria
    template_name = 'curso_materia_list.html'
    context_object_name = 'cursos_materia'

    def get_queryset(self):
        
        auth_user = AuthUser.objects.get(id=self.request.user.id)
        estudiante = Estudiante.objects.get(usuario=auth_user)

        
        materias_seleccionadas = EstudianteMateria.objects.filter(estudiante=estudiante).values_list('curso_materia__id_materia', flat=True)
        return CursoMateria.objects.exclude(id_materia__in=materias_seleccionadas)


@method_decorator(group_required('ESTUDIANTES'), name='dispatch')
class SeleccionarMateria(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        curso_id = request.POST.get('curso_id')
        
        try:
            
            auth_user = AuthUser.objects.get(id=request.user.id)
            estudiante = Estudiante.objects.get(usuario=auth_user)
            curso_materia = CursoMateria.objects.get(id_materia=curso_id)
            
            
            EstudianteMateria.objects.get_or_create(estudiante=estudiante, curso_materia=curso_materia)
            
        except ObjectDoesNotExist as e:
            
            print(e)
            return redirect('error-page')  
        
        return redirect('lista-cursos-materia')  
    
@method_decorator(group_required('ESTUDIANTES'), name='dispatch')   
class ListaCursoMateriaSeleccionada(ListView):
    model = CursoMateria
    template_name = 'curso_materia_seleccionada_list.html'
    context_object_name = 'cursos_materia_seleccionada'

    def get_queryset(self):
        auth_user = AuthUser.objects.get(id=self.request.user.id)
        estudiante = Estudiante.objects.get(usuario=auth_user)
        materias_seleccionadas = EstudianteMateria.objects.filter(estudiante=estudiante).values_list('curso_materia__id_materia', flat=True)
        return CursoMateria.objects.filter(id_materia__in=materias_seleccionadas)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_cost = len(context['cursos_materia_seleccionada']) * 50
        context['total_cost'] = total_cost
        context['metodos_pago'] = PagosMetodo.objects.all()  
        return context
        



class PerfilEstudianteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            # Obtener el usuario autenticado
            auth_user = AuthUser.objects.get(id=request.user.id)
            estudiante = Estudiante.objects.get(usuario=auth_user)
            

        except ObjectDoesNotExist:
            
            return redirect('error-page')
        
        
        return render(request, 'perfil.html', {
            'estudiante': estudiante,        
        })
        



class ProcesarPagoView(View):
    def post(self, request, *args, **kwargs):
        metodo_pago_id = request.POST.get('metodo_pago')
        total_cost = request.POST.get('total_cost')


        metodo_pago = PagosMetodo.objects.get(id_metodo_pago=metodo_pago_id)
        fecha_actual = timezone.now() 
        fecha_formateada = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')
        pago = Pagos(
            estado_pago='PAGADO',
            referencia_pago='REF123456',  
            id_metodo_pago=metodo_pago,
            monto=total_cost,
            fecha_pago=fecha_formateada
        )
        pago.save()
        
        return redirect('perfil-estudiante')  

    def get(self, request, *args, **kwargs):
        return HttpResponse("Operación no permitida", status=405)