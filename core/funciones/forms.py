from django.forms import ModelForm,  widgets
from funciones import models


class Agregar_Pers(ModelForm):
    class Meta:
        model = models.Persona
        fields = '__all__'

        widgets = {
            'fec_nac': widgets.DateInput(attrs = {'type': 'date'}),
        }

class Agre_puesto(ModelForm):
    class Meta:
        model = models.Puesto
        fields = '__all__'
