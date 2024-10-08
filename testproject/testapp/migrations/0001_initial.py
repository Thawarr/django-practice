# Generated by Django 4.2.15 on 2024-08-13 12:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tenant",
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
                ("image", models.ImageField(upload_to="tenantsLogos/")),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("AND", "Android App"),
                            ("IOS", "IOS App"),
                            ("WIN", "Windows"),
                            ("A&I", "Android And IOS"),
                            ("ALL", "All Apps"),
                        ],
                        default="ALL",
                        max_length=3,
                    ),
                ),
            ],
        ),
    ]
