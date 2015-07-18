# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0006_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
