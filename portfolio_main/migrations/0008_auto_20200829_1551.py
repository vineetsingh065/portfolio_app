# Generated by Django 3.1 on 2020-08-29 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_main', '0007_auto_20200828_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='role_description',
            field=models.TextField(max_length=1500),
        ),
    ]