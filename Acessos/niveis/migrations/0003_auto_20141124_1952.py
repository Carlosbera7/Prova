# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('niveis', '0002_validacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='validacao',
            old_name='Local',
            new_name='Descricao',
        ),
    ]
