# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acesso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Descricao', models.CharField(max_length=100, null=True, verbose_name=b'Tipo de Acesso')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Lugar')),
                ('Descricao', models.ManyToManyField(to='niveis.Acesso', null=True, verbose_name=b'Tipo de Acesso')),
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
                ('Descricao', models.ForeignKey(verbose_name=b'Tipo de Acesso', to='niveis.Acesso', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
