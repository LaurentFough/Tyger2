# Generated by Django 2.1.5 on 2019-05-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0004_auto_20190204_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]