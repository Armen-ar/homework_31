# Generated by Django 4.1.1 on 2022-10-02 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_location_user_location_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='location_id',
        ),
    ]