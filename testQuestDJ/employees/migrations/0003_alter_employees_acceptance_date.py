# Generated by Django 4.2.1 on 2024-01-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0002_alter_employees_manager"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employees",
            name="acceptance_date",
            field=models.DateTimeField(),
        ),
    ]
