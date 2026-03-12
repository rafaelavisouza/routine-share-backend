from django.contrib import admin
from django.urls import path
from routines.views import dashboard_view, metas_view, historico_view, concluir_tarefa # <-- Importe a nova função!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('metas/', metas_view, name='metas'),
    path('historico/', historico_view, name='historico'),
    
    # Nova rota para o Check-in:
    path('tarefa/<int:tarefa_id>/concluir/', concluir_tarefa, name='concluir_tarefa'),
]