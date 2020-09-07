# Generated by Django 3.0.5 on 2020-08-17 14:51

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main.validators
import recurrence.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_userpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorPost',
            fields=[
                ('userpost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.UserPost')),
            ],
            options={
                'verbose_name': 'Donor Post',
                'verbose_name_plural': 'Donor Posts',
            },
            bases=('main.userpost',),
        ),
        migrations.CreateModel(
            name='RecipientPost',
            fields=[
                ('userpost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.UserPost')),
            ],
            options={
                'verbose_name': 'Recipient Post',
                'verbose_name_plural': 'Recipient Posts',
            },
            bases=('main.userpost',),
        ),
        migrations.AlterModelOptions(
            name='userpost',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.RemoveField(
            model_name='userpost',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userpost',
            name='user',
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_begin_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_deliver',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_desc',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_end_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_image',
            field=models.ImageField(blank=True, default='default.png', upload_to='profile_pics', validators=[main.validators.validate_is_pic], verbose_name='Profile Image'),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_org_address',
            field=models.CharField(default='123 Test St.', max_length=80, verbose_name='Your Organizations Location'),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_org_city',
            field=models.CharField(default='Stamford', max_length=30),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_org_country',
            field=models.CharField(default='USA', max_length=60),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_org_email',
            field=models.EmailField(default='example@gmail.com', max_length=254, verbose_name='Your Organizations Email'),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_org_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Your Organization'),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_org_phone',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_org_state',
            field=models.CharField(default='CT', max_length=2),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_org_zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_recurring',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userpost',
            name='post_title',
            field=models.CharField(blank=True, max_length=30, verbose_name=''),
        ),
        migrations.CreateModel(
            name='DonorRepeatingPost',
            fields=[
                ('donorpost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.DonorPost')),
                ('recurrences', recurrence.fields.RecurrenceField()),
            ],
            bases=('main.donorpost',),
        ),
        migrations.CreateModel(
            name='RecipientRepeatingPost',
            fields=[
                ('recipientpost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.RecipientPost')),
                ('recurrences', recurrence.fields.RecurrenceField()),
            ],
            bases=('main.recipientpost',),
        ),
    ]