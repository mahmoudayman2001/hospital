# Generated by Django 4.1.4 on 2023-05-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointments", "0002_appoinment_patient_doctor_mobile_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="appoinment",
            name="patient",
        ),
        migrations.AddField(
            model_name="appoinment",
            name="name",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
