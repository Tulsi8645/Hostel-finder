# Generated by Django 4.1.6 on 2023-03-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_userrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
    ]
