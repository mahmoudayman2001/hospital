# Generated by Django 4.1.4 on 2023-05-02 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointments", "0007_remove_doctor_available_days"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appoinment",
            name="day",
            field=models.CharField(
                choices=[
                    ("sat", "sat"),
                    ("sun", "sun"),
                    ("mod", "mod"),
                    ("tues", "tues"),
                    ("wed", "wed"),
                    ("thirs", "thirs"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="appoinment",
            name="time",
            field=models.CharField(
                choices=[
                    ("10", "10"),
                    ("10:30", "10:30"),
                    ("11", "11"),
                    ("11:30", "11:30"),
                    ("12", "12"),
                    ("12:30", "12:30"),
                    ("1", "1"),
                    ("1:30", "1:30"),
                    ("2", "2"),
                ],
                max_length=15,
            ),
        ),
    ]
