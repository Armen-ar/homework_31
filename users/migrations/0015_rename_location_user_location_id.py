# Generated by Django 4.1.1 on 2022-10-02 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_rename_location_id_user_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='location_id',
        ),
    ]
