# Generated by Django 4.1.5 on 2023-02-11 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0015_alter_servicio_desc_sv_alter_servicio_tipo_sv"),
    ]

    operations = [
        migrations.DeleteModel(name="Detalle",),
    ]
