# Generated by Django 3.1.7 on 2021-03-31 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.IntegerField(default=0, verbose_name='Height(cm)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='Weight(kg)'),
        ),
    ]