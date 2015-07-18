# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0007_portfolio_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='static/2015/06'), upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='img',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='static/2015/06'), upload_to=''),
            preserve_default=True,
        ),
    ]
