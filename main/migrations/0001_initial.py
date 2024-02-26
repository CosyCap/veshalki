# Generated by Django 5.0.2 on 2024-02-23 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contacts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Имя")),
                (
                    "phone_number",
                    models.CharField(max_length=15, verbose_name="Номер телефона"),
                ),
                ("email", models.EmailField(max_length=50, verbose_name="Адрес email")),
                ("question", models.TextField()),
            ],
            options={
                "verbose_name": "Заявка",
                "verbose_name_plural": "Заявки",
            },
        ),
    ]