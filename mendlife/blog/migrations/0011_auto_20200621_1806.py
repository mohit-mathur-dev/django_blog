# Generated by Django 3.0.7 on 2020-06-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_tech'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img2',
            field=models.ImageField(blank=True, upload_to='blog/'),
        ),
        migrations.AddField(
            model_name='post',
            name='img3',
            field=models.ImageField(blank=True, upload_to='blog/'),
        ),
        migrations.AddField(
            model_name='post',
            name='img4',
            field=models.ImageField(blank=True, upload_to='blog/'),
        ),
        migrations.AddField(
            model_name='post',
            name='img5',
            field=models.ImageField(blank=True, upload_to='blog/'),
        ),
        migrations.AddField(
            model_name='post',
            name='img6',
            field=models.ImageField(blank=True, upload_to='blog/'),
        ),
    ]