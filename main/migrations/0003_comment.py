# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_publish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='Comment text')),
                ('when', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(to='main.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
