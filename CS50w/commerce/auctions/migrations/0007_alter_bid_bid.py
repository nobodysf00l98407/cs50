# Generated by Django 4.2.5 on 2023-10-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0006_alter_listing_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bid",
            name="bid",
            field=models.IntegerField(),
        ),
    ]
