# Generated by Django 4.0.6 on 2022-09-25 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0008_cashbook_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashbook',
            name='writer',
        ),
    ]
