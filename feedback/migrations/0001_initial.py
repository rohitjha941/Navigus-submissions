# Generated by Django 2.1.7 on 2019-03-08 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=60)),
                ('phone_number', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=128)),
                ('location', models.TextField(max_length=60)),
                ('feedback', models.TextField(max_length=500)),
            ],
        ),
    ]
