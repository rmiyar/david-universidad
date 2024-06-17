from django.urls import path
from django.contrib.auth import views as auth_views
from .views_estudiantes import ListaCursoMateria,SeleccionarMateria

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cursos-materia/', ListaCursoMateria.as_view(), name='lista-cursos-materia'),
    path('seleccionar-materia/', SeleccionarMateria.as_view(), name='seleccionar-materia'),



]