from django.forms import ModelForm
from django import forms
from .models import Reserva

class ReservaForm(ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'cnpj' : forms.TextInput(attrs={'class': 'form-control' }),
            'nome_empresa' : forms.TextInput(attrs={'class': 'form-control' }),
            'categoria' : forms.TextInput(attrs={'class': 'form-control' }),
            'quitado' : forms.CheckboxInput(attrs={'class': 'form-check-input','type':'checkbox'}),  
            'stand' : forms.Select(attrs={'class': 'form-contrl'}),
        }