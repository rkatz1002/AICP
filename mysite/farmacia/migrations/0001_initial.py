# Generated by Django 2.2.2 on 2019-08-03 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo_Brasindice',
            fields=[
                ('ID_Brasindice', models.IntegerField(primary_key=True, serialize=False)),
                ('Brasindice_PMF', models.DecimalField(decimal_places=2, max_digits=18)),
                ('Brasindice_PF', models.DecimalField(decimal_places=2, max_digits=18)),
                ('Simpro', models.DecimalField(decimal_places=2, max_digits=18)),
                ('TUSS', models.CharField(max_length=50)),
                ('TISS', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('ID_Convenio', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo_Farmacologico',
            fields=[
                ('ID_Grupo_Farmacologico', models.IntegerField(primary_key=True, serialize=False)),
                ('Nome_Grupo_Farmacologico', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Historico_Prescricao',
            fields=[
                ('ID_Historico_Prescricao', models.IntegerField(primary_key=True, serialize=False)),
                ('FILESTREAM_Prescricao', models.CharField(max_length=100)),
                ('Data_Historico_Prescricao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('ID_Medicamento_Cadastro', models.IntegerField(primary_key=True, serialize=False)),
                ('Nome_Medicamento', models.CharField(max_length=50)),
                ('Laboratorio', models.CharField(max_length=50)),
                ('Nome_do_Sal', models.CharField(max_length=50)),
                ('Descricao', models.CharField(max_length=50)),
                ('Grupo', models.CharField(max_length=50)),
                ('Quantidade', models.IntegerField()),
                ('ID_Brasindice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.Codigo_Brasindice')),
                ('ID_Convenio_Medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.Convenio')),
                ('ID_Grupo_Farmacologico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.Grupo_Farmacologico')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('ID_Tipo', models.IntegerField(primary_key=True, serialize=False)),
                ('Nome_Tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prescricao_Medicamento',
            fields=[
                ('ID_Prescricao_Medicamento', models.IntegerField(primary_key=True, serialize=False)),
                ('Quantidade_por_dia', models.IntegerField()),
                ('Periodo_inicio', models.DateField()),
                ('Periodo_fim', models.DateField()),
                ('Dosagem', models.IntegerField()),
                ('ID_Historico_Prescricao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.Historico_Prescricao')),
                ('ID_Medicamento_Cadastro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.Medicamento')),
            ],
        ),
        migrations.AddField(
            model_name='medicamento',
            name='ID_Tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.Tipo'),
        ),
    ]
