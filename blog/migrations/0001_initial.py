# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(null=True, default='', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='myblog',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
