# Generated by Django 4.1.6 on 2023-03-08 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_booking_booker_email_booking_bookers_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booker_email',
        ),
    ]
