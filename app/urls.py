from django.urls import path
from django.contrib.auth import views as auth_views
from .views_estudiantes import ListaCursoMateria,SeleccionarMateria,ListaCursoMateriaSeleccionada,PerfilEstudianteView,ProcesarPagoView
from .views_profesores import PerfilProfesorView,EstudiantesMateriaView
from .views import CustomLoginView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cursos-materia/', ListaCursoMateria.as_view(), name='lista-cursos-materia'),
    path('seleccionar-materia/', SeleccionarMateria.as_view(), name='seleccionar-materia'),
    path('materias-seleccionadas/', ListaCursoMateriaSeleccionada.as_view(), name='materias-seleccionadas'),
    path('perfil/', PerfilEstudianteView.as_view(), name='perfil-estudiante'),
    path('procesar-pago/', ProcesarPagoView.as_view(), name='procesar-pago'),
    path('perfil-profesor/', PerfilProfesorView.as_view(), name='perfil-profesor'),
    path('profesor-clase/', EstudiantesMateriaView.as_view(), name='estudiantes-materia'),


]