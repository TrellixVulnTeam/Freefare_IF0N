# Generated by Django 3.0.5 on 2020-08-24 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_userpost_donor_or_recip'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='end_min',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='availability',
            name='start_min',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
