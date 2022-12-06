# Generated by Django 4.1.4 on 2022-12-06 18:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(120), django.core.validators.MinValueValidator(0)]),
        ),
    ]
