# Generated by Django 2.1.5 on 2019-02-02 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.URLField()),
                ('insecure_skip_verify', models.BooleanField(default=False)),
                ('websocket', models.BooleanField(default=False)),
                ('transparent', models.BooleanField(default=False)),
            ],
        ),
    ]
