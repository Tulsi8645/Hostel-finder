# Generated by Django 4.1.6 on 2023-03-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_booking_booker_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booker_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
