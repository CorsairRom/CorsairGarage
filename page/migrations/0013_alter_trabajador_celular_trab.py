# Generated by Django 4.1.5 on 2023-02-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0012_alter_trabajador_tipo_trab"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trabajador",
            name="celular_trab",
            field=models.IntegerField(verbose_name="Número Contacto"),
        ),
    ]