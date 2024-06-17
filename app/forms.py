from django import forms
from app.models import CursoMateria, EstudianteMateria, Estudiante

class InscripcionMateriaForm(forms.ModelForm):
    materias = forms.ModelMultipleChoiceField(
        queryset=CursoMateria.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Estudiante
        fields = ['materias']

    def __init__(self, *args, **kwargs):
        self.estudiante = kwargs.pop('estudiante', None)
        super().__init__(*args, **kwargs)
        if self.estudiante:
            self.fields['materias'].initial = self.estudiante.materias.all()