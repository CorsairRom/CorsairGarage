# Generated by Django 4.1.5 on 2023-02-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0013_alter_trabajador_celular_trab"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicio",
            name="tipo_sv",
            field=models.TextField(blank=True, null=True, verbose_name="Tipo Servicio"),
        ),
    ]
