# Generated by Django 3.0 on 2020-08-29 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ateliere', '0007_auto_20200826_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='image1',
            field=models.ImageField(blank=True, default='', upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image2',
            field=models.ImageField(blank=True, default='', upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image3',
            field=models.ImageField(blank=True, default='', upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image4',
            field=models.ImageField(blank=True, default='', upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image5',
            field=models.ImageField(blank=True, default='', upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image6',
            field=models.ImageField(blank=True, default='', upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]