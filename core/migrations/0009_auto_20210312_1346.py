# Generated by Django 3.1.7 on 2021-03-12 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210312_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.movie'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.person'),
        ),
    ]
