# Generated by Django 4.1.7 on 2023-04-21 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('antiques', '0012_alter_antiques_valuation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='pwd',
        ),
    ]
