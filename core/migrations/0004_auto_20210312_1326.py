# Generated by Django 3.1.7 on 2021-03-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210312_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='boxoffice',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]
