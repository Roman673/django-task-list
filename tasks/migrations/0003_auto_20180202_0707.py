# Generated by Django 2.0.2 on 2018-02-02 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20180202_0652'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]
