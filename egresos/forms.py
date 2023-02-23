from django import forms
from egresos.models import ControlEgresos


class EgresosForm(forms.ModelForm):

    class Meta:
        model = ControlEgresos
        fields = ['autor', 'fecha', 'empresa', 'nombre', 'concepto', 'categoria', 'medio_pago', 'valor']