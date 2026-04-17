from django.contrib import admin

# Register your models here.
from .models import * #importa nossos models

class FabricanteAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'



admin.site.register(Fabricante,FabricanteAdmin) #adiciona a interface do adm
admin.site.register(Categoria)
admin.site.register(Produto)