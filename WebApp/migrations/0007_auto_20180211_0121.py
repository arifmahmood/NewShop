# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-10 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0006_salesrepresentative_mobileno'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasememo',
            name='due',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='purchasememo',
            name='memoTotal',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='salememo',
            name='due',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='salememo',
            name='memoTotal',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
