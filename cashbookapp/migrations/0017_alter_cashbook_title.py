# Generated by Django 4.1.1 on 2022-09-25 08:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0016_alter_cashbook_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashbook',
            name='title',
            field=models.CharField(blank=True, max_length=200, validators=[django.core.validators.MinLengthValidator(0, '글을 써주세요.')]),
        ),
    ]
