# Generated by Django 3.0.5 on 2020-07-29 14:34

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200729_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='org_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
