# Generated by Django 5.0.2 on 2024-03-14 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_alter_recipe_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='created_on',
            field=models.DateField(verbose_name=datetime.datetime(2024, 3, 14, 22, 13, 12, 306024)),
        ),
    ]
