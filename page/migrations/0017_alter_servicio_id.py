# Generated by Django 4.1.5 on 2023-02-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0016_delete_detalle"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicio",
            name="id",
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
