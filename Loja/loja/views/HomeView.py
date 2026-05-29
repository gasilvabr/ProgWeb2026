#from django.http import HttpResponse
from django.shortcuts import render
from loja.models import Produto

def home_view(request):
    # Le nome do produto digitao pelo usuario e consulta banco de dados
    produto = request.GET.get("produto")
    produtos = Produto.objects.all()
    if produto is not None:
        produtos = produtos.filter(Produto__contains=produto)    
    # Monto o contexto comos dados necessarios a visualização da pagina        
    context = {
        'produtos': produtos
    }
    return render(request, template_name='home/home.html', context=context, status=200)