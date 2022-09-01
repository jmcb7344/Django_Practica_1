
from django import forms
from vista_Clases import models


class CursoForm(forms.ModelForm):
    class Meta:
        model = models.Materia
        fields = '__all__'

class EstidianteForm(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = '__all__'

        widgets = {
            'fec_nac' : forms.DateInput(attrs = {'type': 'date'})
        }