# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0006_auto_20170312_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numericsection',
            name='subsection_text',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
