# Generated by Django 4.0.5 on 2023-08-01 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='enable_comment',
            field=models.BooleanField(default=True),
        ),
    ]
