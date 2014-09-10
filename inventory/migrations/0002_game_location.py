# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='location',
            field=models.CharField(default=b'H', max_length=1, choices=[(b'H', b'Home'), (b'W', b'Work'), (b'C', b'Car'), (b'S', b'Sell')]),
            preserve_default=True,
        ),
    ]
