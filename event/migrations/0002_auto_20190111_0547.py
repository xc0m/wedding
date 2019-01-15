# Generated by Django 2.2 on 2019-01-11 05:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='address',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guestOne',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rsvp',
            name='guestTwo',
            field=models.CharField(default='hello', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rsvp',
            name='phonenumber',
            field=models.CharField(default='hello', max_length=255),
            preserve_default=False,
        ),
    ]
