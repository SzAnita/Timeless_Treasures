# Generated by Django 4.1.7 on 2023-04-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiques', '0011_antiques_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antiques',
            name='valuation',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
