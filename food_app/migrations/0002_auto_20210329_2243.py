# Generated by Django 3.1.7 on 2021-03-30 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedbmrresults',
            name='height',
            field=models.IntegerField(default=0, verbose_name='height'),
        ),
        migrations.AddField(
            model_name='savedbmrresults',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='weight'),
        ),
    ]
