from django.urls import path
from egresos.views import Login_user, InsertarRegistro, ListaGastos

urlpatterns = [
    path('insertar-registro/', InsertarRegistro.as_view(), name="registro"),
    path('listagastos/', ListaGastos.as_view(), name="listagastos"),

]