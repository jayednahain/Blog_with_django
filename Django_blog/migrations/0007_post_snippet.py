# Generated by Django 3.1.6 on 2021-02-23 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Django_blog', '0006_auto_20210223_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link for read the full blog post !', max_length=255),
        ),
    ]
