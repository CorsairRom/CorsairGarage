# Generated by Django 4.1.5 on 2023-01-29 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0003_servicio_tipo_sv"),
    ]

    operations = [
        migrations.AlterField(
            model_name="detalle",
            name="id_fi",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="page.ficha_ingreso",
                verbose_name="Número de Ficha",
            ),
        ),
    ]
