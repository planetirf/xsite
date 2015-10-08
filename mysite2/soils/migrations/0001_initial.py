# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GreatGroups',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('greatgroup', models.CharField(unique=True, choices=[('Aquents', (('Cryaquents', 'Cryaquents'), ('Endoaquents', 'Endoaquents'), ('Epiaquents', 'Epiaquents'), ('Fluvaquents', 'Fluvaquents'), ('Gelaquents', 'Gelaquents'), ('Hydraquents', 'Hydraquents'), ('Psammaquents', 'Psammaquents'), ('Sulfaquents', 'Sulfaquents')))], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Soil',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoilOrders',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('order', models.CharField(unique=True, choices=[('Entisols', 'Entisols'), ('Inceptisols', 'Inceptisols'), ('Andisols', 'Andisols'), ('Gelisols', 'Gelisols'), ('Histosols', 'Histosols'), ('Aridisols', 'Aridisols'), ('Vertisols', 'Vertisols'), ('Mollisols', 'Mollisols'), ('Alfisols', 'Alfisols'), ('Spodosols', 'Spodosols'), ('Utilisols', 'Ultisols'), ('Oxisols', 'Oxisols')], max_length=20)),
                ('order_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubOrders',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('suborder', models.CharField(unique=True, choices=[('Entisols', (('Aquents', 'Aquents'), ('Fluvents', 'Fluvents'), ('Orthents', 'Orthents'), ('Psamments', 'Psamments'), ('Wassents', 'Wassents'))), ('Inceptisols', (('Aquepts', 'Aquepts'), ('Cryepts', 'Cryepts'), ('Gelepts', 'Gelepts'), ('Udepts', 'Udepts'), ('Ustepts', 'Ustepts'), ('Xerepts', 'Xerepts'))), ('Andisols', (('Aquands', 'Aquands'), ('Cryands', 'Cryands'), ('Gelands', 'Gelands'), ('Torrands', 'Torrands'), ('Udands', 'Udands'), ('Ustands', 'Ustands'), ('Vitrands', 'Vitrands'), ('Xerands', 'Xerands'))), ('Gelisols', (('Histels', 'Histels'), ('Orthels', 'Orthels'), ('Turbels', 'Turbels'))), ('Histosols', (('Fibrists', 'Fibrists'), ('Folists', 'Folists'), ('Hemists', 'Hemists'), ('Saprists', 'Saprists'), ('Wassists', 'Wassists'))), ('Aridisols', (('Argids', 'Argids'), ('Calcids', 'Calcids'), ('Cambids', 'Cambids'), ('Cryids', 'Cryids'), ('Durids', 'Durids'), ('Gypsids', 'Gypsids'), ('Salids', 'Salids'))), ('Vertisols', (('Aquerts', 'Aquerts'), ('Cryerts', 'Cryerts'), ('Torrerts', 'Torrerts'), ('Uderts', 'Uderts'), ('Usterts', 'Usterts'), ('Xererts', 'Xererts'))), ('Mollisols', (('Albolls', 'Albolls'), ('Aquolls', 'Aquolls'), ('Cryolls', 'Cryolls'), ('Rendolls', 'Rendolls'), ('Udolls', 'Udolls'), ('Ustolls', 'Ustolls'), ('Xerolls', 'Xerolls'))), ('Alfisols', (('Aqualf', 'Aqualf'), ('Cryalf', 'Cryalf'), ('Udalf', 'Udalf'), ('Ustalf', 'Ustalf'), ('Xeralf', 'Xeralf'))), ('Spodosols', (('Aquods', 'Aquods'), ('Cryods', 'Cryods'), ('Humods', 'Humods'), ('Orthods', 'Orthods'))), ('Ultisols', (('Aquults', 'Aquults'), ('Humults', 'Humults'), ('Udults', 'Udults'), ('Usults', 'Usults'), ('Xerults', 'Xerults'))), ('Oxisols', (('Aquox', 'Aquox'), ('Perox', 'Perox'), ('Torrox', 'Torrox'), ('Udox', 'Udox'), ('Ustox', 'Ustox'))), ('unknown', 'Unknown')], max_length=50)),
                ('order', models.ForeignKey(to='soils.SoilOrders')),
            ],
        ),
        migrations.AddField(
            model_name='greatgroups',
            name='suborder',
            field=models.ForeignKey(to='soils.SubOrders'),
        ),
    ]
