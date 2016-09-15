# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('soils', '0003_auto_20151221_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='greatgroups',
            name='order',
            field=models.ForeignKey(to='soils.SoilOrders', default=datetime.datetime(2016, 8, 15, 1, 29, 33, 516379, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
