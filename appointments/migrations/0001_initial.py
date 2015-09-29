# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('when', models.DateTimeField()),
                ('patient', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=96)),
                ('hospital', models.CharField(max_length=64)),
                ('room', models.CharField(max_length=32)),
                ('reason', models.TextField()),
            ],
        ),
    ]
