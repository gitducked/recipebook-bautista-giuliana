# Generated by Django 5.0.2 on 2024-03-14 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0005_alter_recipe_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='update_on',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
