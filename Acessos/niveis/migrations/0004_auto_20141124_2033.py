# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('niveis', '0003_auto_20141124_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='validacao',
            name='Entrada',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='validacao',
            name='Saida',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
    ]
