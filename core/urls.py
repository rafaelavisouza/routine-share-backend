from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from routines.views import dashboard_view, metas_view, historico_view, concluir_tarefa

urlpatterns = [
    # Rota raiz: manda direto para o login
    path("", RedirectView.as_view(url="/login/", permanent=False)),
    
    # Administração
    path('admin/', admin.site.urls),
    
    # Contas e Autenticação (Parte da sua colega)
    path("", include("accounts.urls")),
    
    # Rotinas e Metas (Sua parte)
    path('dashboard/', dashboard_view, name='dashboard'),
    path('metas/', metas_view, name='metas'),
    path('historico/', historico_view, name='historico'),
    path('tarefa/<int:tarefa_id>/concluir/', concluir_tarefa, name='concluir_tarefa'),
]