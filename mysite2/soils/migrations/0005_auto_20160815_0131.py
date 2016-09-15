# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soils', '0004_greatgroups_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greatgroups',
            name='order',
        ),
        migrations.AddField(
            model_name='greatgroups',
            name='order',
            field=models.ManyToManyField(to='soils.SoilOrders'),
        ),
    ]
