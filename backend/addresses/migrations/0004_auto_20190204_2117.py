# Generated by Django 2.1.5 on 2019-02-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0003_remove_address_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.URLField(unique=True),
        ),
    ]
