# Generated by Django 4.1.7 on 2023-04-18 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiques', '0009_antiques_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antiques',
            name='creator',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='antiques',
            name='link',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='antiques',
            name='type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='antiques',
            name='valuation',
            field=models.FloatField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='antiques',
            name='year',
            field=models.CharField(max_length=100),
        ),
    ]
