#from django.http import HttpResponse
from django.shortcuts import render
from loja.models import Produto

def home_view(request):
    # Filtra o produto no banco de dados, criando uma lista com eles
    produto = request.GET.get("produto")
    produtos = Produto.objects.all()
    if produto is not None:
        produtos = produtos.filter(Produto__contains=produto)
    # Cria uma variavel de contexto para passar para o template com a lista
    context = {
        'produtos': produtos
    }
    print(produtos)

    return render(request, template_name='home/home.html', context=context, status=200)