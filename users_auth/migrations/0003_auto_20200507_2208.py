# Generated by Django 3.0.3 on 2020-05-07 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth', '0002_auto_20200507_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todos',
            old_name='backgrond',
            new_name='background',
        ),
    ]
