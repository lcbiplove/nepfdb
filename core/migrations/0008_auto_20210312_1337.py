# Generated by Django 3.1.7 on 2021-03-12 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210312_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='cast',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.cast'),
        ),
        migrations.AlterField(
            model_name='award',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.movie'),
        ),
    ]