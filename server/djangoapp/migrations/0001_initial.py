# Generated by Django 5.1.2 on 2024-10-16 14:02

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarMake",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=200)),
                (
                    "country_of_origin",
                    models.CharField(default="Japan", max_length=100),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CarModel",
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
                ("name", models.CharField(max_length=100)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Sedan", "Sedan"),
                            ("SUV", "SUV"),
                            ("WAGON", "WAGON"),
                        ],
                        default="SUV",
                        max_length=100,
                    ),
                ),
                (
                    "year",
                    models.DateField(
                        default=django.utils.timezone.now,
                        validators=[
                            django.core.validators.MinValueValidator(2015),
                            django.core.validators.MaxValueValidator(2023),
                        ],
                    ),
                ),
                (
                    "car_make",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djangoapp.carmake",
                    ),
                ),
            ],
        ),
    ]
