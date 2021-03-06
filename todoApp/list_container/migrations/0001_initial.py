# Generated by Django 3.0.3 on 2020-10-30 08:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(error_messages={'unique': 'This title is not unique, please try again'}, help_text='Must be a unique title', max_length=100, unique=True)),
                ('details', models.TextField(blank=True, max_length=10000, null=True)),
                ('priority', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('list_container', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='list_container.ListContainer')),
            ],
        ),
    ]
