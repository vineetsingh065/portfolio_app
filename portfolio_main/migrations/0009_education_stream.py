# Generated by Django 3.1 on 2020-08-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_main', '0008_auto_20200829_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='stream',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
    ]
