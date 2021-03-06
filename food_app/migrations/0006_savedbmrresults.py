# Generated by Django 3.1.7 on 2021-04-03 03:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_app', '0005_auto_20210329_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedBmrResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(default=0, verbose_name='weight')),
                ('height', models.IntegerField(default=0, verbose_name='height')),
                ('age', models.IntegerField(default=0, verbose_name='age')),
                ('sex', models.CharField(default='-', max_length=50, verbose_name='sex')),
                ('bmr_result', models.FloatField(blank=True, default=0, verbose_name='bmrresult')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
