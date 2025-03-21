# Generated by Django 4.2.19 on 2025-03-11 04:08

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='us_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='US', unique=True),
        ),
    ]
