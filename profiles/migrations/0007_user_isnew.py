# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20150926_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isNew',
            field=models.BooleanField(default=True),
        ),
    ]
