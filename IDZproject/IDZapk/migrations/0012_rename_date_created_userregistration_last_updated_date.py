# Generated by Django 4.0.6 on 2022-10-04 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IDZapk', '0011_alter_userregistration_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregistration',
            old_name='date_created',
            new_name='last_updated_date',
        ),
    ]