# Generated by Django 4.1.1 on 2022-10-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_rename_location_user_location_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='is_activ',
            field=models.BooleanField(default=True),
        ),
    ]
