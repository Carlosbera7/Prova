# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('niveis', '0004_auto_20141124_2033'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='validacao',
            unique_together=set([('Nome', 'Descricao')]),
        ),
    ]
