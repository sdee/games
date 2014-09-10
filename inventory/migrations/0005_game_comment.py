# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_genre_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='comment',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
    ]
