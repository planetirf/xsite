# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soils', '0002_auto_20151221_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suborders',
            name='suborder',
            field=models.CharField(choices=[('Entisols', (('Aquents', 'Aquents'), ('Fluvents', 'Fluvents'), ('Orthents', 'Orthents'), ('Psamments', 'Psamments'), ('Wassents', 'Wassents'))), ('Inceptisols', (('Aquepts', 'Aquepts'), ('Cryepts', 'Cryepts'), ('Gelepts', 'Gelepts'), ('Udepts', 'Udepts'), ('Ustepts', 'Ustepts'), ('Xerepts', 'Xerepts'))), ('Andisols', (('Aquands', 'Aquands'), ('Cryands', 'Cryands'), ('Gelands', 'Gelands'), ('Torrands', 'Torrands'), ('Udands', 'Udands'), ('Ustands', 'Ustands'), ('Vitrands', 'Vitrands'), ('Xerands', 'Xerands'))), ('Gelisols', (('Histels', 'Histels'), ('Orthels', 'Orthels'), ('Turbels', 'Turbels'))), ('Histosols', (('Fibrists', 'Fibrists'), ('Folists', 'Folists'), ('Hemists', 'Hemists'), ('Saprists', 'Saprists'), ('Wassists', 'Wassists'))), ('Aridisols', (('Argids', 'Argids'), ('Calcids', 'Calcids'), ('Cambids', 'Cambids'), ('Cryids', 'Cryids'), ('Durids', 'Durids'), ('Gypsids', 'Gypsids'), ('Salids', 'Salids'))), ('Vertisols', (('Aquerts', 'Aquerts'), ('Cryerts', 'Cryerts'), ('Torrerts', 'Torrerts'), ('Uderts', 'Uderts'), ('Usterts', 'Usterts'), ('Xererts', 'Xererts'))), ('Mollisols', (('Albolls', 'Albolls'), ('Aquolls', 'Aquolls'), ('Cryolls', 'Cryolls'), ('Gellolls', 'Gellolls'), ('Rendolls', 'Rendolls'), ('Udolls', 'Udolls'), ('Ustolls', 'Ustolls'), ('Xerolls', 'Xerolls'))), ('Alfisols', (('Aqualf', 'Aqualf'), ('Cryalf', 'Cryalf'), ('Udalf', 'Udalf'), ('Ustalf', 'Ustalf'), ('Xeralf', 'Xeralf'))), ('Spodosols', (('Aquods', 'Aquods'), ('Cryods', 'Cryods'), ('Humods', 'Humods'), ('Orthods', 'Orthods'))), ('Ultisols', (('Aquults', 'Aquults'), ('Humults', 'Humults'), ('Udults', 'Udults'), ('Usults', 'Usults'), ('Xerults', 'Xerults'))), ('Oxisols', (('Aquox', 'Aquox'), ('Perox', 'Perox'), ('Torrox', 'Torrox'), ('Udox', 'Udox'), ('Ustox', 'Ustox'))), ('unknown', 'Unknown')], max_length=50, unique=True),
        ),
    ]
