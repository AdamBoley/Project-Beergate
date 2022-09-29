# Generated by Django 3.2.15 on 2022-09-29 06:21

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20220922_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='alcohol',
            field=models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(Decimal('0.0'))]),
        ),
    ]
