# Generated by Django 4.1.4 on 2023-05-02 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointments", "0004_doctor_available_days"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="available_days",
            field=models.CharField(
                choices=[
                    ("1", "sat"),
                    ("2", "sun"),
                    ("3", "mod"),
                    ("4", "tues"),
                    ("5", "wed"),
                    ("6", "thirs"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
