# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Animal(models.Model):
    animal_codigo = models.AutoField(primary_key=True)
    apelido = models.CharField(max_length=100)
    nascimento = models.DateField()
    tutor_codigo = models.ForeignKey('Tutor', models.DO_NOTHING, db_column='tutor_codigo')
    raca_codigo = models.ForeignKey('Raca', models.DO_NOTHING, db_column='raca_codigo')

    class Meta:
        managed = False
        db_table = 'animal'


class AquisicaoProduto(models.Model):
    aquisicao_codigo = models.AutoField(primary_key=True)
    produto_codigo = models.ForeignKey('Produto', models.DO_NOTHING, db_column='produto_codigo')
    quantidade = models.IntegerField()
    data_aquisicao = models.DateField()

    class Meta:
        managed = False
        db_table = 'aquisicao_produto'


class Atendimento(models.Model):
    atendimento_sequencia = models.AutoField(primary_key=True)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    situacao_codigo = models.ForeignKey('Situacao', models.DO_NOTHING, db_column='situacao_codigo')
    animal_codigo = models.ForeignKey(Animal, models.DO_NOTHING, db_column='animal_codigo')
    parcelas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atendimento'


class AtendimentoProduto(models.Model):
    atendimento_produto_sequencia = models.AutoField(primary_key=True)
    atendimento_sequencia = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='atendimento_sequencia')
    produto_codigo = models.ForeignKey('Produto', models.DO_NOTHING, db_column='produto_codigo')
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atendimento_produto'


class AtendimentoServico(models.Model):
    atendimento_servico_sequencia = models.AutoField(primary_key=True)
    atendimento_sequencia = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='atendimento_sequencia')
    servico_codigo = models.ForeignKey('Servico', models.DO_NOTHING, db_column='servico_codigo')
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atendimento_servico'


class AtendimentoVacina(models.Model):
    atendimento_vacina_sequencia = models.AutoField(primary_key=True)
    atendimento_sequencia = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='atendimento_sequencia')
    vacina_codigo = models.ForeignKey('Vacina', models.DO_NOTHING, db_column='vacina_codigo')
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atendimento_vacina'


class Categoria(models.Model):
    categoria_codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'categoria'


class Especie(models.Model):
    especie_codigo = models.AutoField(primary_key=True)
    descricao = models.CharField()

    class Meta:
        managed = False
        db_table = 'especie'


class Fornecedor(models.Model):
    fornecedor_codigo = models.AutoField(primary_key=True)
    razao = models.CharField()
    contato = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'fornecedor'


class Parcela(models.Model):
    parcela_sequencia = models.AutoField(primary_key=True)
    atendimento_sequencia = models.ForeignKey(Atendimento, models.DO_NOTHING, db_column='atendimento_sequencia')
    numero = models.IntegerField()
    vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento = models.DateField(blank=True, null=True)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'parcela'


class Pedido(models.Model):
    pedido_numero = models.AutoField(primary_key=True)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    situacao = models.CharField(max_length=100)
    fornecedor_codigo = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='fornecedor_codigo')

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoProduto(models.Model):
    pedido_produto_sequencia = models.AutoField(primary_key=True)
    pedido_pedido_numero = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='pedido_pedido_numero')
    produto_produto_codigo = models.ForeignKey('Produto', models.DO_NOTHING, db_column='produto_produto_codigo')
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pedido_produto'


class Produto(models.Model):
    produto_codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria_codigo = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria_codigo')

    class Meta:
        managed = False
        db_table = 'produto'


class Raca(models.Model):
    raca_codigo = models.AutoField(primary_key=True)
    descricao = models.CharField()
    especie_codigo = models.ForeignKey(Especie, models.DO_NOTHING, db_column='especie_codigo')

    class Meta:
        managed = False
        db_table = 'raca'


class Servico(models.Model):
    servico_codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_codigo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='tipo_codigo')

    class Meta:
        managed = False
        db_table = 'servico'


class Situacao(models.Model):
    situacao_codigo = models.AutoField(primary_key=True)
    descricao = models.CharField()

    class Meta:
        managed = False
        db_table = 'situacao'


class Tipo(models.Model):
    tipo_codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    desconto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tipo'


class Tutor(models.Model):
    tutor_codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    saldodevedor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tutor'


class Vacina(models.Model):
    vacina_codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'vacina'
