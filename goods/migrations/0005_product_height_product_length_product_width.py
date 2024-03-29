# Generated by Django 5.0.2 on 2024-02-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0004_alter_product_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="height",
            field=models.DecimalField(
                decimal_places=2, default=0.0, max_digits=7, verbose_name="Высота"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="length",
            field=models.DecimalField(
                decimal_places=2, default=0.0, max_digits=7, verbose_name="Длина"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="width",
            field=models.DecimalField(
                decimal_places=2, default=0.0, max_digits=7, verbose_name="Ширина"
            ),
        ),
    ]
