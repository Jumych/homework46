# Generated by Django 4.1.3 on 2022-11-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='mОписание'),
        ),
    ]
