# Generated by Django 4.2.1 on 2023-05-18 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='slug',
        ),
    ]
