# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0007_auto_20170401_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numericsection',
            name='subsection_text',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
