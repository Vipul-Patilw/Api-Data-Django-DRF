# Generated by Django 4.0.3 on 2022-09-09 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IDZapk', '0004_alter_userregistration_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='mobile_number',
            field=models.CharField(max_length=100),
        ),
    ]
