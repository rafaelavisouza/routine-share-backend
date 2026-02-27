from django.shortcuts import render

# Create your views here.
def dashboard_view(request):
    return render(request, 'dashboard.html')

def metas_view(request):
    return render(request, 'metas.html')

def historico_view(request):
    return render(request, 'historico.html')