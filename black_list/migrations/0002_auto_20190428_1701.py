# Generated by Django 2.1.4 on 2019-04-28 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('black_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToekenBlackList',
            new_name='TokenBlackList',
        ),
    ]
