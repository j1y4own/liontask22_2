# Generated by Django 4.0.6 on 2022-09-25 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0011_cashbook_created_at_alter_cashbook_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashbook',
            name='pub_date',
        ),
    ]
