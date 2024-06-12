# Generated by Django 5.0.3 on 2024-06-11 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fire", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="firefighters",
            name="experience_level",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Beginner", "Beginner"),
                    ("Intermediate", "Intermediate"),
                    ("Advanced", "Advanced"),
                    ("Expert", "Expert"),
                ],
                max_length=45,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="firefighters",
            name="rank",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Probationary Firefighter", "Probationary Firefighter"),
                    ("Firefighter I", "Firefighter I"),
                    ("Firefighter II", "Firefighter II"),
                    ("Firefighter III", "Firefighter III"),
                    ("Driver", "Driver"),
                    ("Captain", "Captain"),
                    ("Battalion Chief", "Battalion Chief"),
                ],
                max_length=45,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="firefighters",
            name="station",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="firefighters",
                to="fire.firestation",
            ),
        ),
        migrations.AlterField(
            model_name="firetruck",
            name="capacity",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="incident",
            name="date_time",
            field=models.DateField(blank=True, null=True),
        ),
    ]
