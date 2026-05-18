from django.http import HttpResponse
from loja.models import Produto

def list_produto_view(request, id=None):
    # Carrega dados do navegador
    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    # carrego dados do baco de dados
    #produtos = Produto.objects.all()
    #produtos = Produto.objects.first()
    produtos = Produto.objects.filter(Produto=produto)
    print(produtos)
    if destaque is not None:
        print(destaque)
    if produto is not None:
        print(produto)
    if promocao is not None:
        print(promocao)
    if categoria is not None:
        print(categoria)
    if fabricante is not None:
        print(fabricante)
    
    #if id is None:
    #    id = 0
    if id is None:
        return HttpResponse('<h1>Nenhum id foi informado</h1>')
    return HttpResponse('<h1>Produto de id %s!</h1>' % id)