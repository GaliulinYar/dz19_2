# Generated by Django 4.2.3 on 2023-08-24 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'версия', 'verbose_name_plural': 'версии'},
        ),
    ]
