from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from egresos.models import ControlEgresos
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Login_user(TemplateView):
    template_name = 'egresos/index.html'

class InsertarRegistro(CreateView, ListView):
    model = ControlEgresos
    fields = ['autor', 'fecha', 'empresa', 'nombre', 'concepto', 'categoria', 'medio_pago', 'valor']
    success_url = reverse_lazy('registro')
    template_name = 'egresos/registrar.html'
    queryset = ControlEgresos.objects.all().order_by('id').reverse()[:10]


class ListaGastos(ListView):
    model = ControlEgresos
    template_name = 'egresos/listagastos.html'
    queryset = ControlEgresos.objects.all().order_by('-fecha')


    
    

