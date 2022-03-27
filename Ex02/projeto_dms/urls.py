from django.contrib import admin
from django.urls import path

from app_copa.views import CampeonatoList, DetalheCampeonato, CriarCampeonato, AtualizarCampeonato, CancelarCampeonato, RankingList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', CampeonatoList.as_view(template_name="copa/index.html"), name='leer'),
    path('index/ranking', RankingList.as_view(template_name="copa/ranking.html"), name='ranking'),
    path('index/detalhe/<int:pk>', DetalheCampeonato.as_view(template_name="copa/detalhes.html"), name='detalhes'),
    path('index/criar', CriarCampeonato.as_view(template_name="copa/criar.html"), name='criar'),
    path('index/editar/<int:pk>', AtualizarCampeonato.as_view(template_name="copa/editar.html"), name='editar'),
    path('index/delete/<int:pk>', CancelarCampeonato.as_view(), name='delete'),
]
