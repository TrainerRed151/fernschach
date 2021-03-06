# Generated by Django 3.1.3 on 2020-12-07 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=32)),
                ('salt', models.CharField(max_length=8)),
                ('elo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(max_length=256)),
                ('black', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='black', to='spiel.player')),
                ('white', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='white', to='spiel.player')),
            ],
        ),
    ]
