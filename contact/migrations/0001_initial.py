# Generated by Django 2.1.7 on 2019-03-07 22:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=60)),
                ('last_name', models.CharField(default='', max_length=60)),
                ('email', models.EmailField(default='', max_length=128)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
