# Generated by Django 3.1.7 on 2021-03-12 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210312_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='desc',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='desc',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]