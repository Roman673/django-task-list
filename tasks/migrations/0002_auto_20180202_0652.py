# Generated by Django 2.0.2 on 2018-02-02 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['created_by']},
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='updated_by',
        ),
    ]
