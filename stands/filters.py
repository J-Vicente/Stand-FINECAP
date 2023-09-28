import django_filters
from .models import Reserva

class ReservaFilter(django_filters.FilterSet):
    class Meta:
        model = Reserva
        fields = ['nome_empresa', 'quitado', 'stand__valor','data']