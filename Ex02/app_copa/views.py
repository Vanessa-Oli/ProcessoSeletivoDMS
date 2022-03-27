from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Campeonato
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms


class CampeonatoList(ListView):
    model = Campeonato


class CriarCampeonato(SuccessMessageMixin, CreateView):
    model = Campeonato
    form = Campeonato
    fields = "__all__"
    success_message = 'Campeonato criado'

    def get_success_url(self):
        return reverse('leer')


class DetalheCampeonato(DetailView):
    model = Campeonato


class AtualizarCampeonato(SuccessMessageMixin, UpdateView):
    model = Campeonato
    form = Campeonato
    fields = "__all__"
    success_message = 'Placar Atualizado !'

    def get_success_url(self):
        return reverse('leer')

class CancelarCampeonato(SuccessMessageMixin, DeleteView):
    model = Campeonato
    form = Campeonato
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Campeonato Cancelado'
        messages.success(self.request, (success_message))
        return reverse('leer')
class RankingList(TemplateView):
    template_name = 'copa/ranking.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rankings = []
        competicoes = Campeonato.objects.all()
        for competicao in competicoes:
           rankings = {}
        context['rankings'] = rankings
        return context