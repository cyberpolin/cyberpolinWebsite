# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_auto_20150228_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('alt', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('latlon', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
