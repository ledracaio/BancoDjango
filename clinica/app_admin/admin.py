from django.contrib import admin
from app_admin.models import Animal, Atendimento, AtendimentoProduto, AtendimentoServico, AtendimentoVacina, Categoria
from app_admin.models import Especie, Fornecedor, Parcela, Pedido, Produto, PedidoProduto, Raca, Servico, Situacao, Tipo, Tutor, Vacina




@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'desconto')
    search_fields = ('descricao',)




@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'desconto')
    search_fields = ('descricao',)    




@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)




@admin.register(Situacao)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)




@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'especie_codigo')
    search_fields = ('descricao',)




@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('razao', 'contato')
    search_fields = ('razao',)    




@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato', 'saldodevedor')
    search_fields = ('nome',)




@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('apelido', 'nascimento', 'raca_codigo', 'tutor_codigo')
    search_fields = ('apelido',)    




@admin.register(Vacina)
class VacinaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor')
    search_fields = ('descricao',)  




@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'tipo_codigo')
    search_fields = ('descricao',)        




@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'categoria_codigo', 'estoque')
    search_fields = ('descricao',)  




class PedidoProdutoInLine(admin.TabularInline):
    model = PedidoProduto
    raw_in_fields = ['pedido_numero']




@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('data', 'valor', 'situacao', 'fornecedor_codigo')
    list_filter = ('fornecedor_codigo',)
    search_fields = ('data',)  
    ordering = ('-data',)
    date_hierarchy = 'data'
    inlines = [PedidoProdutoInLine]


class AtendimentoProdutoInLine(admin.TabularInline):
    model = AtendimentoProduto
    raw_in_fields = ['atendimento_sequencia']


class AtendimentoServicoInLine(admin.TabularInline):
    model = AtendimentoServico
    raw_in_fields = ['atendimento_sequencia']


class AtendimentoVacinaInLine(admin.TabularInline):
    model = AtendimentoVacina
    raw_in_fields = ['atendimento_sequencia']


class ParcelaInLine(admin.TabularInline):
    model = Parcela
    raw_in_fields = ['atendimento_sequencia']


@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('data', 'valor', 'situacao_codigo', 'animal_codigo', 'parcelas')
    list_filter = ('animal_codigo',)
    search_fields = ('data',)  
    ordering = ('-data',)
    date_hierarchy = 'data'
    inlines = [AtendimentoProdutoInLine, AtendimentoServicoInLine, AtendimentoVacinaInLine, ParcelaInLine]
