# Generated by Django 4.2.14 on 2024-07-23 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo_list',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
