# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('niveis', '0002_auto_20141125_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validacao',
            name='Entrada',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
