# Generated by Django 2.2.4 on 2019-10-03 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piracy_prevention_api', '0004_auto_20191003_0530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activationlist',
            old_name='auth_machine',
            new_name='authorized_machine',
        ),
    ]
