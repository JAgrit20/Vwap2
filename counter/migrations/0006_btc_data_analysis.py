# Generated by Django 4.1.5 on 2023-01-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("counter", "0005_btc_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="btc_data", name="Analysis", field=models.TextField(blank=True),
        ),
    ]
