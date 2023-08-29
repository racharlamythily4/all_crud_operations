# Generated by Django 4.2.3 on 2023-08-26 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "topic_name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Webpage",
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
                ("url", models.URLField(default="http://mythily.in")),
                (
                    "topic_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.topic"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Accessrecords",
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
                ("date", models.DateField(auto_now=True)),
                ("author", models.CharField(max_length=100)),
                (
                    "email",
                    models.EmailField(default="mythily@gmail.com", max_length=254),
                ),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.webpage"
                    ),
                ),
            ],
        ),
    ]
