# Generated by Django 5.0.1 on 2024-02-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPP', '0002_rename_togri_soz_notogrisoz_togrisoz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notogrisoz',
            name='soz',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='togrisoz',
            name='soz',
            field=models.CharField(max_length=250),
        ),
    ]
