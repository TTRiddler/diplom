# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 15:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0004_auto_20170226_1102'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='algebraicsection',
            table='AlgebraicSection',
        ),
        migrations.AlterModelTable(
            name='algebraicsystem',
            table='AlgebraicSystem',
        ),
        migrations.AlterModelTable(
            name='numericsection',
            table='NumericSection',
        ),
        migrations.AlterModelTable(
            name='numericsystem',
            table='NumericSystem',
        ),
    ]