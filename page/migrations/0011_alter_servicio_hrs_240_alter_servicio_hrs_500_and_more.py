# Generated by Django 4.1.5 on 2023-02-11 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0010_alter_servicio_hrs_240_alter_servicio_hrs_500_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicio",
            name="hrs_240",
            field=models.PositiveIntegerField(verbose_name="Horas hasta 240 cc"),
        ),
        migrations.AlterField(
            model_name="servicio",
            name="hrs_500",
            field=models.PositiveIntegerField(verbose_name="Horas hasta 500 cc"),
        ),
        migrations.AlterField(
            model_name="servicio",
            name="hrs_800",
            field=models.PositiveIntegerField(verbose_name="Horas hasta 800 cc"),
        ),
        migrations.AlterField(
            model_name="servicio",
            name="hrs_810",
            field=models.PositiveIntegerField(verbose_name="Horas desde 810 cc"),
        ),
    ]
