from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, Goal
from django.shortcuts import render, redirect, get_object_or_404

@login_required(login_url='/login/')
def dashboard_view(request):
    # 1. Busca todas as tarefas no banco que pertencem ao usuário logado
    tarefas_do_usuario = Task.objects.filter(usuario=request.user)
    
    # 2. Empacota essas tarefas em um dicionário de contexto
    context = {
        'tarefas': tarefas_do_usuario
    }
    
    # 3. Envia o contexto para o HTML
    return render(request, 'dashboard.html', context)

# Adicionamos a proteção de login, pois a tarefa precisa de um 'usuario' para ser salva
@login_required(login_url='/login/')
def metas_view(request):
    if request.method == 'POST':
        tipo_form = request.POST.get('tipo_form')
        
        # Salvando TAREFAS (Aba 1)
        if tipo_form == 'tarefa':
            Task.objects.create(
                titulo=request.POST.get('titulo'),
                descricao=request.POST.get('descricao'),
                categoria=request.POST.get('categoria'),
                dificuldade=request.POST.get('dificuldade'),
                usuario=request.user
            )
            return redirect('metas')
            
# Salvando METAS (Aba 2)
        elif tipo_form == 'meta':
            Goal.objects.create(
                titulo=request.POST.get('titulo_meta'),
                # Apagamos a linha da categoria que estava aqui!
                tipo=request.POST.get('tipo_meta'),
                usuario=request.user
            )
            return redirect('metas')

    # Busca as metas cadastradas pelo usuário para exibir na direita
    metas_do_usuario = Goal.objects.filter(usuario=request.user)
    
    context = {
        'metas': metas_do_usuario
    }
    return render(request, 'metas.html', context)

@login_required(login_url='/login/')
def historico_view(request):
    # Busca APENAS as tarefas que estão concluídas
    tarefas_finalizadas = Task.objects.filter(usuario=request.user, concluida=True)
    
    # 1. Conta quantas tarefas foram concluídas
    total_tarefas = tarefas_finalizadas.count()
    
    # 2. Soma os pontos (F=10, M=20, D=30)
    total_pontos = 0
    for tarefa in tarefas_finalizadas:
        if tarefa.dificuldade == 'F':
            total_pontos += 10
        elif tarefa.dificuldade == 'M':
            total_pontos += 20
        elif tarefa.dificuldade == 'D':
            total_pontos += 30
            
    # 3. Metas (Como ainda não criamos o botão de concluir Metas, deixamos 0 por enquanto para ser honesto)
    total_metas = 0

    # Empacota as variáveis para mandar para o HTML
    context = {
        'tarefas_concluidas': tarefas_finalizadas,
        'total_tarefas': total_tarefas,
        'total_pontos': total_pontos,
        'total_metas': total_metas,
    }
    
    return render(request, 'historico.html', context)

@login_required(login_url='/login/')
def concluir_tarefa(request, tarefa_id):
    # Busca a tarefa específica que pertence ao usuário logado
    tarefa = get_object_or_404(Task, id=tarefa_id, usuario=request.user)
    
    # Se ela ainda não estiver concluída, marca como concluída e salva!
    if not tarefa.concluida:
        tarefa.concluida = True
        tarefa.save()
        
        # 💡 DICA: É exatamente AQUI que, no futuro, nós vamos adicionar 
        # a lógica de somar os pontos no Profile do usuário!
        
    # Recarrega o dashboard
    return redirect('dashboard')