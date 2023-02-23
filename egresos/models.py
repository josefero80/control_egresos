from django.db import models
from django.contrib.auth.models import User

# Create your models here.

choices_empresa = [
    (1, 'FloralGroup'),
    (2, 'FloralCargo'),
    (3, 'FloralHome')
]

choices_categoria = [
    (1, 'marketing'),
    (2, 'nomina'),
    (3, 'mercancias'),
    (4, 'contabilidad'),
    (5, 'fletes'),
    (6, 'impuestos'),
    (7, 'vehiculos'),
    (8, 'cafeteria'),
    (9, 'servicios publicos'),
    (10, 'bodega'),
    (11, 'oficina'),
    (12, 'prestamos'),
    (13, 'aseo'),
    (14, 'arriendos'),
    (15, 'otros')
]

choices_medio_pago = [
    (1, 'nequi'),
    (2, 'daviplata_jf'),
    (3, 'efectivo'),
    (4, 'daviplata_dc'),
    (5, 'bancolombia_cargo'),
    (6, 'bancolombia_home'),
    (7, 'tc_bancolombia'),
    (8, 'bancolombia_aho_fg'),
    (9, 'bancolombia_cte_fg')
]

class ControlEgresos(models.Model):

    id = models.AutoField(primary_key=True, serialize=True)
    autor = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING)
    fecha = models.DateField(null=False, blank=False)
    empresa = models.IntegerField(null=False, blank=False, choices=choices_empresa) 
    nombre = models.CharField(max_length=255, null=False, blank=False)
    concepto = models.CharField(max_length=255, null=False, blank=False)
    categoria = models.IntegerField(null=False, blank=False, choices=choices_categoria)
    medio_pago = models.IntegerField(null=False, blank=False, choices=choices_medio_pago)
    valor = models.FloatField(null=False, blank=False, default=0)

    class Meta:
        managed = True
        db_table = 'egresos_controlegresos'

    def __str__(self):
        return f'{self.fecha} {self.empresa} {self.concepto} {self.categoria}'
