# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20150926_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='relation',
            field=models.CharField(choices=[('se', 'Self'), ('ga', 'Guardian'), ('sp', 'Spouse'), ('fa', 'Father'), ('mo', 'Mother'), ('si', 'Sibling'), ('ch', 'Child'), ('ot', 'Other')], max_length=2),
        ),
    ]
