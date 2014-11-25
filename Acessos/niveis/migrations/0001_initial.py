# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Lugar')),
                ('Descricao', models.CharField(max_length=1, null=True, verbose_name=b'Acesso', choices=[(b'1', b'LIVRE'), (b'2', b'RESTRITO'), (b'3', b'RESERVADO')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('Endereco', models.CharField(max_length=100, null=True, verbose_name=b'Endere\xc3\xa7o')),
                ('Telefone', models.CharField(max_length=15, null=True, verbose_name=b'Telefone')),
                ('Descricao', models.CharField(max_length=1, null=True, verbose_name=b'Acesso', choices=[(b'1', b'LIVRE'), (b'2', b'RESTRITO'), (b'3', b'RESERVADO')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='validacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Entrada', models.TimeField(null=True)),
                ('Saida', models.TimeField(null=True)),
                ('Local', models.ForeignKey(verbose_name=b'Local', to='niveis.Lugar', null=True)),
                ('Nome', models.ForeignKey(verbose_name=b'Pessoa', to='niveis.Pessoa', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='validacao',
            unique_together=set([('Nome', 'Local')]),
        ),
    ]
