# Generated by Django 4.2.3 on 2023-08-28 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_webpage_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accessrecords", name="date", field=models.DateField(),
        ),
    ]
