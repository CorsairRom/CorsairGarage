# Generated by Django 4.1.5 on 2023-01-29 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0004_alter_detalle_id_fi"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehiculo",
            name="modelo_vh",
            field=models.CharField(
                default="DEFAULT MODEL", max_length=50, verbose_name="Modelo"
            ),
        ),
    ]
