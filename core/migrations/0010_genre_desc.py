# Generated by Django 3.1.7 on 2021-03-12 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210312_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='desc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
