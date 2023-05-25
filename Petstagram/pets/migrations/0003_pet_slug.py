# Generated by Django 4.2.1 on 2023-05-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_remove_pet_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='slug',
            field=models.SlugField(default='none', unique=True),
            preserve_default=False,
        ),
    ]