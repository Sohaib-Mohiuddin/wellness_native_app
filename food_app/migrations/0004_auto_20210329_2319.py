# Generated by Django 3.1.7 on 2021-03-30 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0003_auto_20210329_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedbmiresults',
            name='bmi_result',
            field=models.IntegerField(blank=True, verbose_name='bmiresult'),
        ),
    ]
