
from django.urls import  reverse_lazy
from django.contrib.auth import views as auth_views
from .models import AuthUser, Estudiante, Profesor
from django.contrib.auth.models import User

class CustomLoginView(auth_views.LoginView):
    def get_success_url(self):
        auth_user = AuthUser.objects.get(id=self.request.user.id)
        
        try:
            estudiante = Estudiante.objects.get(usuario=auth_user)
            return reverse_lazy('perfil-estudiante')
        except Estudiante.DoesNotExist:
            try:
                profesor = Profesor.objects.get(usuario=auth_user)
                return reverse_lazy('perfil-profesor')
            except Profesor.DoesNotExist:
                return reverse_lazy('home')  # Redirigir a una página por defecto si no es estudiante ni profesor

