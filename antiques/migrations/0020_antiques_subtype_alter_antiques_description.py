# Generated by Django 4.2.1 on 2023-05-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiques', '0019_alter_antiques_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='antiques',
            name='subtype',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='antiques',
            name='description',
            field=models.CharField(max_length=750),
        ),
    ]
