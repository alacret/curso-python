# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0002_articulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('comentario', models.CharField(max_length=120)),
                ('articulo', models.ForeignKey(to='web_site.Articulo')),
                ('autor', models.ForeignKey(to='web_site.Persona')),
            ],
        ),
    ]
