# Generated by Django 4.0.6 on 2022-09-25 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0004_remove_cashbook_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashbook',
            name='writer',
            field=models.CharField(default='천우', max_length=20),
        ),
    ]
