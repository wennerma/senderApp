# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textIt', '0003_auto_20160908_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='provider',
            field=models.CharField(choices=[('TMOBILE', 'T-Mobile'), ('VERIZON', 'Verizon'), ('CRICKET', 'Cricket'), ('SPRINT', 'Sprint'), ('att', 'AT&T')], max_length=20, null=True),
        ),
    ]
