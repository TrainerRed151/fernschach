# Generated by Django 3.1.3 on 2021-01-11 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='board',
        ),
        migrations.AddField(
            model_name='game',
            name='history',
            field=models.CharField(default='', max_length=2048),
        ),
    ]
