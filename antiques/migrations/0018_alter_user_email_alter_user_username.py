# Generated by Django 4.1.7 on 2023-04-26 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiques', '0017_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
