# Generated by Django 3.0.7 on 2020-07-05 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0006_wcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='writing',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
