# Generated by Django 2.0.6 on 2018-12-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='View Count'),
        ),
    ]