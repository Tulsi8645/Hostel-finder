# Generated by Django 4.1.6 on 2023-03-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_hostel_rooms_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='rooms_available',
            field=models.JSONField(blank=True, null=True, verbose_name='Rooms Available'),
        ),
    ]
