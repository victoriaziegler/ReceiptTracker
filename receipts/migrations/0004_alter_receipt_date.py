# Generated by Django 4.0.5 on 2022-06-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0003_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
