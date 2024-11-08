# Generated by Django 5.1.2 on 2024-11-04 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('animal_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('apelido', models.CharField(max_length=100)),
                ('nascimento', models.DateField()),
            ],
            options={
                'db_table': 'animal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('atendimento_sequencia', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('parcelas', models.IntegerField()),
            ],
            options={
                'db_table': 'atendimento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AtendimentoProduto',
            fields=[
                ('atendimento_produto_sequencia', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
            ],
            options={
                'db_table': 'atendimento_produto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AtendimentoServico',
            fields=[
                ('atendimento_servico_sequencia', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
            ],
            options={
                'db_table': 'atendimento_servico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AtendimentoVacina',
            fields=[
                ('atendimento_vacina_sequencia', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
            ],
            options={
                'db_table': 'atendimento_vacina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'categoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('especie_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField()),
            ],
            options={
                'db_table': 'especie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('fornecedor_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('razao', models.CharField()),
                ('contato', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'fornecedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parcela',
            fields=[
                ('parcela_sequencia', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('vencimento', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pagamento', models.DateField(blank=True, null=True)),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'parcela',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('pedido_numero', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('situacao', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PedidoProduto',
            fields=[
                ('pedido_produto_sequencia', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
            ],
            options={
                'db_table': 'pedido_produto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('produto_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estoque', models.IntegerField()),
            ],
            options={
                'db_table': 'produto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('raca_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField()),
            ],
            options={
                'db_table': 'raca',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('servico_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'servico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('situacao_codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('descricao', models.CharField()),
            ],
            options={
                'db_table': 'situacao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('tipo_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'tipo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('tutor_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('contato', models.CharField(max_length=100)),
                ('saldodevedor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'tutor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('vacina_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'vacina',
                'managed': False,
            },
        ),
    ]
