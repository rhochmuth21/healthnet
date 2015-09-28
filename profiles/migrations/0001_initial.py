# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('firstName', models.CharField(max_length=32)),
                ('middleInitial', models.CharField(max_length=1)),
                ('lastName', models.CharField(max_length=64)),
                ('phoneNumber', models.CommaSeparatedIntegerField(max_length=10)),
                ('address', models.CharField(max_length=1000)),
                ('relation', models.CharField(choices=[('ga', 'Guardian'), ('sp', 'Spouse'), ('fa', 'Father'), ('mo', 'Mother'), ('ch', 'Child'), ('ot', 'Other')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('accountType', models.CharField(default='P', choices=[('P', 'Patient'), ('D', 'Doctor'), ('A', 'Admin'), ('N', 'Nurse')], max_length=1)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='profiles.User', primary_key=True, serialize=False)),
                ('birthdate', models.DateField()),
                ('height', models.CommaSeparatedIntegerField(max_length=5)),
                ('weight', models.IntegerField()),
                ('insurance', models.CharField(max_length=200)),
                ('allergies', models.TextField()),
                ('conditions', models.TextField()),
                ('prescriptions', models.TextField()),
                ('hospitalPref', models.CharField(max_length=200)),
            ],
            bases=('profiles.user',),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(to='profiles.User'),
        ),
    ]
