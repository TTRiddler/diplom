# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 07:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Numeric',
            new_name='AlgebraicSystem',
        ),
        migrations.RenameModel(
            old_name='Algebraic',
            new_name='NumericSystem',
        ),
    ]