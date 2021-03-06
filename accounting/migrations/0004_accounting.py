# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-24 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_balance_sheet_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('history', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('debit', models.CharField(max_length=100)),
                ('credit', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('conta_devedora', models.CharField(max_length=200)),
                ('conta_credora', models.CharField(max_length=200)),
            ],
        ),
    ]
