# Generated by Django 3.1 on 2020-08-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_main', '0004_auto_20200827_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='user_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
